import os
import re
import trie
import PyPDF2
import pickle
import word_class as wc

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False 
    cont = 0

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
    #60-62: se verifica que la direccion sea un directorio 
    if not os.path.isdir(path):
        print("The provided path is not a directory")
        return
    #64-66: se crea una lista que contiene todo el texto de cada pdf
    pdfs = []
    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    # 68: crea una lista con todos los nombres de los archivos ["archivo.pdf",...]
    list_arch = os.listdir(path)
    #71: lista para guardar los trie
    list_trie = []
    # 74-77: las lista con los nombres de los archivos pasa a ser una lisata con datos del tipo Archivo()
    # y se guardan los nombres de cada archivo en cada posicion (archivo.name)
    for i in range(len(list_arch)):
        a=Archivo()
        a.name = list_arch[i]
        list_arch[i] = a
    
    #81-88: el str original d cada archivo se "limpia" y se guarda una lista con 
    # el trie de cada archivo 
    for pdf in pdfs:
        t=Trie()
        for term in pdf.split(' '):
            for word in separate(term):
                c_word = wc.clean(word)
                if is_classifiable(c_word):
                    trie.insert(t,c_word)
        list_trie.append(t)
        
         
    #92-93: se guarda el trie y el nombre de cada archivo en una lista 
    for i in range(len(list_arch)):
            list_arch[i].tree = list_trie[i]
    #96-98: se guarda un archivo con una lista de pdfs con su nombre y trie respectivamente
    # en memoria  
    with open("list_arch.pkl","wb") as f:
        pickle.dump(list_arch,f)
        print("document data-base created successfully")

if __name__ == "__main__":

    create("/Users/Fran/OneDrive/Documentos/proyecto_algo2_2024/proyecto-algo2-1/proyecto-algo2-1/code/test_pdfs")

    with open("list_arch.pkl","rb") as f:
        archivos_list = pickle.load(f)

    print("LECTURA DE ARCHIVO")
    for i in range(len(archivos_list)):
        print("---- ", archivos_list[i].name)
        trie.leeTrie(archivos_list[i].tree.root.children,"",False,0)
    
