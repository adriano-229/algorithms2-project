import os
import re

import PyPDF2

import classification_db as cl


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


def replace_all(text):
    for sym, _ in cl.extra.items():
        text = text.replace(sym, _)
    return text


def clean_term(t):
    clean_t = t.lower()
    clean_t = re.findall(r'\b[a-zA-Záéíóúñ0-9-!¡¿?]+\b', clean_t)
    if len(clean_t) == 1:
        return replace_all(clean_t[0])
    return None


def is_classifiable(word):
    if not word:
        return False
    if len(word) < 3:
        return False
    if word in cl.pronombres:
        return False
    if word in cl.preposiciones:
        return False
    return True


def create(path):
    if not os.path.isdir(path):
        return "The provided path is not a directory"

    pdfs = []

    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    words = []

    for pdf in pdfs:
        terms = pdf.split(' ')

        for term in terms:
            word = clean_term(term)
            if is_classifiable(word):  # colocar filtro de palabras innecesarias
                words.append(word)
                print(word, end=' ')


if __name__ == "__main__":
    create("/home/admin1/Documents/proyecto-algo2/code/pdfs_prueba")
