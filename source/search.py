from formatting import remove_keys, associate_names, sort_present_dicc
from parsing import *
from pickles_ import *
from similitude import compare_cosine_similarity


def search(text):
    if not text:
        print("document not found")
        return

    filenames = pickle_load(DB_FILENAMES)
    tf_list = pickle_load(DB_TF_LIST)
    main_empty_vec = pickle_load(DB_MAIN_EMPTY_VEC)

    corpus_size = len(filenames) + 1

    word_lists = create_word_lists_from_texts([text])[0]
    for word in word_lists:
        for tf in tf_list:
            tf[word] = tf.get(word, 0)
        main_empty_vec[word] = main_empty_vec.get(word, 0)

    search_tf = calculate_term_frequencies([word_lists], main_empty_vec)
    tf_list += search_tf
    idf = calculate_inverse_document_frequencies(main_empty_vec, tf_list, corpus_size)
    tfidf_vec_list = calculate_tfidf_vectors(tf_list, idf)

    create_vectors = remove_keys(tfidf_vec_list)
    search_vector = create_vectors.pop()
    del corpus_size, idf, main_empty_vec, search_tf, text, tf_list, tfidf_vec_list

    compare = compare_cosine_similarity(create_vectors, search_vector)
    result = associate_names(filenames, compare)
    if not sort_present_dicc(result):
        print("document not found")
    return


if __name__ == "__main__":
    search("""Argentina""")

# POSIBLES UPDATES
# - Incluir limpieza de prefijos, sufijos y plurales
# - Investigar diferentes formas de similitud y/o mejoras del tf-idf (por ej.: n-gramas)
# - Incorporar un TAD que refine palabras, como el Trie
