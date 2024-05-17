import math
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


def tf_idf_tables(pdf, idf):
    tf = {}
    tot = 0
    for term in pdf.split(' '):
        words = separate(term)
        for word in words:
            word = wc.clean(word)
            if not word:
                continue
            tot += 1

            tf[word] = tf.get(word, 0) + 1
            if tf[word] == 1:
                idf[word] = idf.get(word, 0) + 1

    for key, _ in tf.items():
        tf[key] /= tot
    return tf




def create(path):
    if not os.path.isdir(path):
        print("The provided path is not a directory")
        return

    pdfs = []
    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    n = len(pdfs)

    weights_list= []
    idf_general = {}
    for pdf in pdfs:
        weights_list.append(tf_idf_tables(pdf, idf_general))

    for table in weights_list:
        for key, value in table.items():
            tf_ = table[key]
            idf_ = math.log2(n / value)
            table[key] = round(tf_ * idf_, 4)

    for table in weights_list:
        for weights_list in sorted(table, key=table.get, reverse=True):
            print(weights_list, table[weights_list])
        print(' ')


if __name__ == "__main__":
    create(
        "/home/admin1/Documents/Universidad/2do/Algoritmos 2/proyecto-algo2/code/test_pdfs")  # poner el dir adecuado
