import copy
import math
import os
import pickle
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


def extract_texts_from_pdfs(path):
    corpus = os.listdir(path)
    pdfs_str = []
    for file in corpus:
        pdf_s = pdf2str(path, file)
        pdfs_str.append(pdf_s)
    return pdfs_str


def convert_texts_to_word_lists(pdfs_str):
    word_lists = []
    for pdf_s in pdfs_str:
        word_lst = create_word_list(pdf_s)
        word_lists.append(word_lst)
    return word_lists


def create_main_vector(word_lists):
    main_vec = {}
    for word_lst in word_lists:
        create_dicc(main_vec, word_lst)
    return main_vec


def calculate_term_frequencies(word_lists, main_vec):
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
    return tf_list


def calculate_inverse_document_frequencies(main_empty_vec, tf_list, corpus_size):
    idf = copy.deepcopy(main_empty_vec)
    for tf in tf_list:
        for word in tf.keys():
            if tf[word] > 0:
                idf[word] += 1
        for word in idf.keys():
            if idf[word] != 0:
                idf[word] = math.log2(corpus_size / idf[word])
            else:
                idf[word] = 0
    return idf


def calculate_tfidf_vectors(tf_list, idf):
    tfidf_vec_list = []
    for tf in tf_list:
        tfidf_vec = {}
        for word in tf.keys():
            tfidf_vec[word] = tf[word] * idf[word]
        tfidf_vec_list.append(tfidf_vec)
    return tfidf_vec_list


def pickle_dump(file, name):
    with open(name, 'bw') as f:
        pickle.dump(file, f)
    # print('Dumped successfully!')
    return


def pickle_load(name):
    with open(name, 'br') as file:
        ld = pickle.load(file)
    # print('Loaded successfully!')
    return ld


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

    corpus_pdfs_str = extract_texts_from_pdfs(path)
    all_word_lists = convert_texts_to_word_lists(corpus_pdfs_str)
    main_empty_vec = create_main_vector(all_word_lists)
    tf_list = calculate_term_frequencies(all_word_lists, main_empty_vec)
    idf = calculate_inverse_document_frequencies(main_empty_vec, tf_list, len(corpus_pdfs_str))
    tfidf_vec_list = calculate_tfidf_vectors(tf_list, idf)

    pickle_dump(main_empty_vec, "main_empty_vec")
    pickle_dump(tfidf_vec_list, "tfidf_vec_list")
    print("document data-base created successfully")

    # x = pickle_load("tfidf_vec_list")
    # pass
    #
    # for vec in x:
    #     for w, ti in vec.items():
    #         print(w, ti)
    #     print()


if __name__ == "__main__":
    create(
        "/home/admin1/Documents/Universidad/2do/Algoritmos 2/proyecto-algo2/code/test_pdfs")  # poner el dir adecuado
