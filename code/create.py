import os
import re

import PyPDF2


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


def clean_words(txt):
    clean_words = []

    terms = txt.split(" ")
    for t in terms:
        lower_t = t.lower()
        clean_t = re.findall(r'\b[a-zA-Záéíóúñ0-9-]+\b', lower_t)
        word = ""
        if len(clean_t) > 0:
            clean_t = clean_t[0].split("-")
            for w in clean_t:
                word += w
            clean_words.append(word)
    return clean_words


def create(path):
    if not os.path.isdir(path):
        return "The provided path is not a directory"

    pdfs = []

    for file in os.listdir(path):
        pdfs.append(pdf2str(path, file))

    words = []

    for pdf in pdfs:
        words.append(clean_words(pdf))

    for w in words:
        txt = ""
        for word in w:
            txt += word + ' '
        print(txt)


if __name__ == "__main__":
    create("/home/admin1/Documents/proyecto-algo2/code/pdfs_prueba")
