import os
import re
import trie
import PyPDF2
import pickle
import word_class as wc

class Archivo:
    name = None
    tree = None


def pdf2str(path, file):
    with open(os.path.join(path, file), 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        txt = ""

        for p in range(len(reader.pages)):
            txt += reader.pages[p].extract_text()
    return txt


def str2words(txt):
    words = []

    for s in txt:
        words.append(s.split(" "))
    return words


def separate(term):
    lowered = term.lower()
    separate = re.findall(r'[a-zA-ZñÑáéíóúÁÉÍÓÚ]+|\d+', lowered)
    return separate


def is_classifiable(word):
    if len(word) < 3 or word in wc.descartes:
        return False
    try:
        n = int(word)
        if n not in range(1000, 3001):
            return False
    except:
        pass
    return True


def create(path):
    if not os.path.isdir(path):
        print("The provided path is not a directory")
        return

    pdfs = []
    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    list_arch = os.listdir(path)

    for i in range(len(list_arch)):
        a=Archivo()
        a.name = list_arch[i]
        list_arch[i] = a

    ListaTries = []

    for pdf in pdfs:
        d = trie.Trie()
        raiz = trie.TrieNode()
        d.root = raiz
        bigrama = ""
        contador = 0
        for term in pdf.split(' '):
            for word in separate(term):
                c_word = wc.clean(word)
                c_word = wc.cleanprefix(c_word)
                if is_classifiable(c_word)==True:
                    palabra = c_word
                    contador += 1
                    bigrama = bigrama + c_word
                if contador==2:
                    trie.Insert(d,bigrama)
                    contador = 1
                    bigrama = palabra

        ListaTries.append(d)

    for i in range(len(list_arch)):
        list_arch[i].tree = ListaTries[i]

    with open("pdf","wb") as f:
        pickle.dump(list_arch,f)

if __name__ == "__main__":
    create("/Users/facul/Onedrive/Escritorio/ProyectoAlgo2/proyecto-algo2/code/test_pdfs4")  # poner el directorio adecuado
    with open("pdf","rb") as f:
        Triepdf = pickle.load(f)

    TextoPROFE ="La medicina es la ciencia que estudia la salud y la enfermedad en los seres humanos. La anatomía investiga la estructura del cuerpo humano. La fisiología analiza las funciones y procesos corporales. La farmacología estudia los efectos de los fármacos en el organismo. La epidemiología examina la distribución y determinantes de las enfermedades en poblaciones."
    ListaMatcheados = []
    bigrama = ""
    contador = 0
    contadormatch = 0
    for T in Triepdf:
        for term in TextoPROFE.split(' '):
                for word in separate(term):
                    c_word = wc.clean(word)
                    c_word = wc.cleanprefix(c_word)
                    if is_classifiable(c_word)==True:
                        palabra = c_word
                        contador += 1
                        bigrama = bigrama + c_word
                    if contador==2:
                        contadormatch = contadormatch + trie.matcheador(T.tree,bigrama,1)
                        contador = 1
                        bigrama = palabra


        ListaMatcheados.append(contadormatch)
        contadormatch = 0
    print(ListaMatcheados)
    indice = 0
    maximos = {}
    max = 0
    if len(ListaMatcheados)>=3:
        eta = 3
    else:
        eta = len(ListaMatcheados) 

    for j in range(0,eta):
        for i in range(0,len(ListaMatcheados)):
            if ListaMatcheados[i]>max:
                max = ListaMatcheados[i]
                indice = i
        ListaMatcheados[indice] = 0
        maximos[Triepdf[indice].name] = max
        max = 0
    print(maximos)

""""
 if is_classifiable(c_word)==False:
                    contadorFalso = 1
                    contador += 1
                    trigrama = trigrama + c_word
                else:
                    contadorVerdadero = 1
                    contador += 1
                    trigrama = trigrama + c_word
                if contador ==3:
                    if contadorVerdadero==1 and contadorFalso==1 or contadorVerdadero==2:
                        trie.Insert(d,bigrama)
                    bigrama = ""
                    contadorFalso = 0
                    contadorVerdadero = 0
                    contador = 0   
"""