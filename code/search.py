from parsing import *
from pickles import *


def search(text):
    db_tf_list = pickle_load("tf_list")
    db_main_empty_vec = pickle_load("main_empty_vec")
    word_lists = create_word_lists_from_texts([text])[0]

    for word in word_lists:
        for tf in db_tf_list:
            tf[word] = tf.get(word, 0)
        db_main_empty_vec[word] = db_main_empty_vec.get(word, 0)

    search_tf = calculate_term_frequencies([word_lists], db_main_empty_vec)
    db_tf_list += search_tf

    idf = calculate_inverse_document_frequencies(db_main_empty_vec, db_tf_list, len(search_tf) + 1)
    tfidf_vec_list = calculate_tfidf_vectors(db_tf_list, idf)
    pass


if __name__ == "__main__":
    search("abcdefghijklmnopqrst hola messi asado tenis perro perro perro perro")
