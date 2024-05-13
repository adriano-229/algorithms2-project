import os
import re

import PyPDF2

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


def hash_freq_counter(pdf):
    dic = dict()
    tot = 0
    for term in pdf.split(' '):
        words = separate(term)
        for word in words:
            c_word = wc.clean(word)
            # if not is_classifiable(c_word):
            #     continue
            tot += 1
            dic[word] = dic.get(word, 0) + 1
    for key, value in dic.items():
        dic[key] = value / tot
    print(dic)
    return dic


def create(path):
    if not os.path.isdir(path):
        print("The provided path is not a directory")
        return

    pdfs = []
    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    dicts = []
    for pdf in pdfs:
        dicts.append(hash_freq_counter(pdf))



if __name__ == "__main__":
    create("/home/admin1/Documents/proyecto-algo2/code/test_pdfs")  # poner el directorio adecuado
