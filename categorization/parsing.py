
import os
import re
from categorization.word_wastes import *
import PyPDF2


def pdf2str(path, file): #Funcion que se encarga de hacer uso de la libreria
    with open(os.path.join(path, file), 'rb') as f:
        reader = PyPDF2.PdfReader(f)

        txt = ""
        for p in range(len(reader.pages)):
            txt += reader.pages[p].extract_text()
    txt.replace(" ", "")
    return txt


def create_texts_from_pdfs(path): #Convierte los archivos pdf a str
    corpus = os.listdir(path)
    pdfs_str = {}
    for file in corpus:
        pdf = pdf2str(path, file)
        pdfs_str[file] = pdf
    return pdfs_str


def create_word_lists_from_texts(pdfs_str): #Crea los tokens de cada palabra para luego pasarlos a bigramas

    def create_word_list(string):
        word_list = []
        terms = string.split(' ')
        for term in terms:
            words = re.findall(r'[a-zA-ZñÑáéíóúÁÉÍÓÚ]+|\d+', term.lower())
            for word in words:
                word = clean(word)
                if word:
                    word_list.append(word)
        for i in range(len(word_list)-1):
            word_list[i] = word_list[i] + " " + word_list[i+1]
        return word_list

    word_lists = []
    for pdf_s in pdfs_str:
        word_lst = create_word_list(pdf_s)
        word_lists.append(word_lst)
    return word_lists

def calculate_term_frequencies(word_lists): #Calcula la aparicion de cada palabra en su respectivo documento
    tf_list = []
    for word_lst in word_lists:
        tf = {}
        for word in word_lst:
            tf[word] = tf.get(word,0) + 1
        for word in tf.keys():
            count = tf[word]
            if count != 0:
                tf[word] = count / len(word_lst)
        tf_list.append(tf)
    return tf_list


def calculate_inverse_document_frequencies(tf_list): #Calcula unicamente en cuantos documentos aparece una palabra
    idf = {}
    for tf in tf_list:
        for word in tf.keys():

            idf[word] = idf.get(word,0) + 1

    return idf


def calculate_tfidf_vectors(tf_list, idf): #Calcula finalmente el valor tf-idf
    tfidf_vec_list = []
    for tf in tf_list:
        tfidf_vec = {}
        for word in tf.keys():
            tfidf_vec[word] = tf[word] * idf[word]
        tfidf_vec_list.append(tfidf_vec)
    return tfidf_vec_list
