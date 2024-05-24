from categorization.parsing import *
from create import DB_FILENAMES, DB_TF_LIST, DB_MAIN_EMPTY_VEC
from pickles import *


def remove_keys(dic_list):
    lst = []
    for dic in dic_list:
        lst.append(list(dic.values()))
    return lst


def associate_names(names_lst, ele_lst):
    dic = {}
    if len(names_lst) != len(ele_lst):
        raise Exception("associate_names error!")

    for i in range(len(names_lst)):
        dic[names_lst[i]] = ele_lst[i]
    return dic


def search(text):
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
    tfidf_vec_list = remove_keys(tfidf_vec_list)

    # tfidf_vec_list = associate_names(filenames, tfidf_vec_list) TODO, terminar procesamiento coseno + asociación ans

    pass


if __name__ == "__main__":
    search("abcdefghijklmnopqrst hola messi asado tenis perro perro perro perro")
