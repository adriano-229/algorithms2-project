import os
import re
import trie
import PyPDF2
import pickle
import word_class as wc


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
    ListaTries = []
    for pdf in pdfs:
        print(pdfs)
        d = trie.Trie()
        for term in pdf.split(' '):
            for word in separate(term):
                c_word = wc.clean(word)
                c_word = wc.cleanprefix(c_word)
                if is_classifiable(c_word):
                    if trie.matcheador(d,c_word)==False:
                        trie.insert(d,wc.cleanprefix(c_word))
                    
        trie.leeTrie(d.root.children,"",False,0)
        ListaTries.append(d)
    with open("pdf","wb") as f:
        pickle.dump(ListaTries,f)

if __name__ == "__main__":
    create("/Users/facul/Onedrive/Escritorio/ProyectoAlgo2/proyecto-algo2/code/test_pdfs")  # poner el directorio adecuado

    with open("pdf","rb") as f:
        Triepdf = pickle.load(f)
    print(Triepdf)
    trie.leeTrie(Triepdf[0].root.children,"",False,0)