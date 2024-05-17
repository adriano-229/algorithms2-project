import os
import re
import trie
import PyPDF2

import word_class as wc

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False 
    cont = 0

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

    #valid_words = [] ; se implementa un trie por eso se deja de usar la lista 

    list_trie=[]
    for pdf in pdfs:
        t=Trie()
        for term in pdf.split(' '):
            for word in separate(term):
                c_word = wc.clean(word)
                if is_classifiable(c_word):
                    #valid_words.append(c_word) ; se deja de usar lista 
                    #print(c_word, end=' ') # todo: empezar a implementar Trie desde acá
                    trie.insert(t,c_word)
        #trie.leeTrie(t.root.children,"",False,0)
        list_trie.append(t)
#falta implementar de manera correcta el pickl y resolver el problema de nombres para el pickl 

if __name__ == "__main__":
    #create("/home/admin1/Documents/proyecto-algo2/code/test_pdfs")  # poner el directorio adecuado
    #create("/Users/Fran/OneDrive/Documentos/proyecto_algo2_2024/proyecto-algo2-1/proyecto-algo2-1/code/test_pdfs")
    create("/Users/Fran/OneDrive/Documentos/proyecto_algo2_2024/proyecto-algo2-1/proyecto-algo2-1/code/test_pdfs")
