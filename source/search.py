from categorization.parsing import *
from pickles import *


def search(text):
    DB_TF_LIST = pickle_load("FILENAME_DB_TF_LIST")
    DB_MAIN_EMPTY_VEC = pickle_load("FILENAME_DB_MAIN_EMPTY_VEC")
    word_lists = create_word_lists_from_texts([text])[0]

    for word in word_lists:
        for tf in DB_TF_LIST:
            tf[word] = tf.get(word, 0)
        DB_MAIN_EMPTY_VEC[word] = DB_MAIN_EMPTY_VEC.get(word, 0)

    search_tf = calculate_term_frequencies([word_lists], DB_MAIN_EMPTY_VEC)
    DB_TF_LIST += search_tf

    idf = calculate_inverse_document_frequencies(DB_MAIN_EMPTY_VEC, DB_TF_LIST, len(search_tf) + 1)
    tfidf_vec_list = calculate_tfidf_vectors(DB_TF_LIST, idf)
    pass


if __name__ == "__main__":
    search("abcdefghijklmnopqrst hola messi asado tenis perro perro perro perro")
