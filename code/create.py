import copy
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
        words.append(s.split(' '))
    return words


def separate(term):
    low = term.lower()
    sep = re.findall(r'[a-zA-ZñÑáéíóúÁÉÍÓÚ]+|\d+', low)
    return sep


def create_word_list(string):
    word_list = []

    terms = string.split(' ')
    for term in terms:
        words = separate(term)
        for word in words:
            word = wc.clean(word)
            if word:
                word_list.append(word)
    return word_list


def create_dicc(dicc, lst):
    for e in lst:
        if e not in dicc:
            dicc[e] = 0
    return dicc


def create(path):
    if not os.path.isdir(path):
        quit("The provided path is not a directory")

    pdfs_str = []
    corpus = os.listdir(path)
    corpus_size = len(corpus)

    for file in corpus:
        pdf_s = pdf2str(path, file)
        pdfs_str.append(pdf_s)
    del file, pdf_s, path, corpus

    word_lists = []
    for pdf_s in pdfs_str:
        word_lst = create_word_list(pdf_s)
        word_lists.append(word_lst)
    del pdfs_str, pdf_s, word_lst

    main_vec = {}
    for word_lst in word_lists:
        create_dicc(main_vec, word_lst)
    del word_lst

    tf_list = []
    for word_lst in word_lists:
        tf = copy.deepcopy(main_vec)
        for word in word_lst:
            tf[word] += 1
        for word in tf.keys():
            count = tf[word]
            if count != 0:
                tf[word] = count / len(word_lst)
        tf_list.append(tf)
    del tf, word_lists, word_lst, word, count

    idf = copy.deepcopy(main_vec)
    for tf in tf_list:
        for word in tf.keys():
            if tf[word] > 0:
                idf[word] += 1
        for word in idf.keys():
            if idf[word] != 0:
                idf[word] = math.log2(corpus_size / idf[word])
            else:
                idf[word] = 0
    del tf, word

    tfidf_vec_list = []
    for tf in tf_list:
        tfidf_vec = {}
        for word in tf.keys():
            tfidf_vec[word] = tf[word] * idf[word]
        tfidf_vec_list.append(tfidf_vec)
    del idf, tf, tf_list, tfidf_vec, word, corpus_size

    for vec in tfidf_vec_list:
        for w, ti in vec.items():
            print(w, ti)
        print()

    # todo PICKLE DE LOS VECTORES, ENCAPSULAR FUNCIONES Y EMPEZAR EL SEARCH


if __name__ == "__main__":
    create(
        "/home/admin1/Documents/Universidad/2do/Algoritmos 2/proyecto-algo2/code/test_pdfs")  # poner el dir adecuado
