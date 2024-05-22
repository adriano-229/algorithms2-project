from parsing import *
from pickles import *


def search(text):
    word_lists = create_word_lists_from_texts([text])[0]

    db_tf_list = pickle_load("tf_list")
    db_main_empty_vec = pickle_load("main_empty_vec")

    for word in word_lists:
        if word not in db_main_empty_vec:
            for tf in db_tf_list:
                tf[word] = 0
            db_main_empty_vec[word] = 0

    tf_list = calculate_term_frequencies([word_lists], db_main_empty_vec)
    db_tf_list += tf_list

    idf = calculate_inverse_document_frequencies(db_main_empty_vec, db_tf_list, len(tf_list) + 1)
    tfidf_vec_list = calculate_tfidf_vectors(db_tf_list, idf)
    pass


if __name__ == "__main__":
    search("abcdefghijklmnopqrst hola messi asado tenis perro perro perro perro")
