import copy
import math
import os
import re

import PyPDF2

import word_wastes as wc


def pdf2str(path, file):
    with open(os.path.join(path, file), 'rb') as f:
        reader = PyPDF2.PdfReader(f)

        txt = ""
        for p in range(len(reader.pages)):
            txt += reader.pages[p].extract_text()
    return txt


def create_texts_from_pdfs(path):
    corpus = os.listdir(path)
    pdfs_str = {}
    for file in corpus:
        pdf = pdf2str(path, file)
        pdfs_str[file] = pdf
    return pdfs_str


def create_word_lists_from_texts(pdfs_str):
    def create_word_list(string):
        word_list = []

        terms = string.split(' ')
        for term in terms:
            words = re.findall(r'[a-zA-ZñÑáéíóúÁÉÍÓÚ]+|\d+', term.lower())
            for word in words:
                word = wc.clean(word)
                if word and word not in wc.descartes:
                    word_list.append(word)
        return word_list

    word_lists = []
    for pdf_s in pdfs_str:
        word_lst = create_word_list(pdf_s)
        word_lists.append(word_lst)
    return word_lists


def create_main_vector(word_lists):
    main_vec = {}
    for word_lst in word_lists:
        for word in word_lst:
            main_vec[word] = main_vec.get(word, 0)
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
    return idf


def calculate_tfidf_vectors(tf_list, idf):
    tfidf_vec_list = []
    for tf in tf_list:
        tfidf_vec = {}
        for word in tf.keys():
            tfidf_vec[word] = tf[word] * idf[word]
        tfidf_vec_list.append(tfidf_vec)
    return tfidf_vec_list
