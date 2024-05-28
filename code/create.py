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
        for term in pdf.split(' '):
            for word in separate(term):
                c_word = wc.clean(word)
                c_word = wc.cleanprefix(c_word)
                if is_classifiable(c_word):
                    if trie.matcheador(d,c_word,0)==False:
                        trie.Insert(d,c_word)
        ListaTries.append(d)
    for i in range(len(list_arch)):
        list_arch[i].tree = ListaTries[i]
    with open("pdf","wb") as f:
        pickle.dump(list_arch,f)

if __name__ == "__main__":
    create("/Users/facul/Onedrive/Escritorio/ProyectoAlgo2/proyecto-algo2/code/test_pdfs2")  # poner el directorio adecuado
    with open("pdf","rb") as f:
        Triepdf = pickle.load(f)
    
    TextoPROFE = "La ingeniería es una disciplina que aplica principios científicos y matemáticos para diseñar, desarrollar y optimizar sistemas, estructuras y procesos. En ingeniería mecánica, se analizan la dinámica de fluidos, la termodinámica y la resistencia de materiales, utilizando herramientas como el análisis de elementos finitos (FEA) y la dinámica de sistemas multicuerpo. La ingeniería eléctrica abarca circuitos, electromagnetismo y sistemas de control, empleando teoría de redes y transformadas de Fourier. En ingeniería civil, se diseñan infraestructuras como puentes y edificios, utilizando métodos de análisis estructural y mecánica de suelos. La ingeniería de software implica el desarrollo de algoritmos, estructuras de datos y la gestión de proyectos mediante metodologías ágiles y control de versiones"
    contador = 0
    ListaMatcheados = []
    for T in Triepdf:
        for term in TextoPROFE.split(' '):
                for word in separate(term):
                    c_word = wc.clean(word)
                    c_word = wc.cleanprefix(c_word)
                    if is_classifiable(c_word):
                        contador = contador + trie.matcheador(T.tree,c_word,1)        

        ListaMatcheados.append(contador)
        contador = 0
    print(ListaMatcheados)
    maximos = {}
    max = 0
    for j in range(0,3):
        for i in range(0,len(ListaMatcheados)):
            if ListaMatcheados[i]>max:
                max = ListaMatcheados[i]
                indice = i
        ListaMatcheados[indice] = 0
        maximos[Triepdf[indice].name] = max
        max = 0
    print(maximos)
    print("---------------")
    print(Triepdf[51].name)
    print(ListaMatcheados[51])
    print(Triepdf[50].name)
    print(ListaMatcheados[50])
    print(Triepdf[49].name)
    print(ListaMatcheados[49])

