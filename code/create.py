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


def clean(word):
    for sym, rpl in wc.cambios.items():
        word = word.replace(sym, rpl)
    return word


def is_classifiable(word):
    if len(word) < 3 or word in list(wc.pronombres) + list(wc.preposiciones):
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
        return "The provided path is not a directory"

    pdfs = []
    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    valid_words = []
    for pdf in pdfs:
        for term in pdf.split(' '):
            for word in separate(term):

                word = clean(word)
                if is_classifiable(word):
                    valid_words.append(word)
                    # print(word, end=' ')


if __name__ == "__main__":
    create("/code/test_pdfs")
