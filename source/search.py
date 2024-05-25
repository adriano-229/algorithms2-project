import operator

from create import DB_FILENAMES, DB_TF_LIST, DB_MAIN_EMPTY_VEC
from parsing import *
from pickles import *
from similitude import cosine_similarity


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


def compare_cosine_similarity(vec_set, vec):
    ans = []
    for v in vec_set:
        simil = round(cosine_similarity(v, vec) * 100, 1)
        ans.append(simil)
    return ans


def sort_present_dicc(dicc):
    def format_percentage(value, decimals=2):
        width = decimals + 3
        return f"{value:>{width}.{decimals}f} %"

    tot = 0
    for value in dicc.values():
        tot += value
        if tot == 0:
            tot = 0.01
    for file, value in dicc.items():
        dicc[file] = round(value / tot * 100, 2)
    lst = dicc.items()
    lst = sorted(lst, key=operator.itemgetter(1), reverse=True)
    for file, ans in lst:
        print(f"{format_percentage(ans)} — {file}")
    return lst


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
    del word, corpus_size, idf, main_empty_vec, search_tf, tf_list, tf

    tfidf_vec_list = remove_keys(tfidf_vec_list)
    search_vector = tfidf_vec_list.pop()
    db_vectors = tfidf_vec_list

    compare = compare_cosine_similarity(db_vectors, search_vector)
    result = associate_names(filenames, compare)
    result = sort_present_dicc(result)
    return result


if __name__ == "__main__":
    search("""
En el análisis de todo ese periodo, se muestra la menor dedicación al
estudio por parte de los que no han obtenido el título de GESO y de los que
tienen el título de CFGM, frente a los que obtuvieron el GESO y el título
de bachillerato. No obstante, la participación en el mercado de trabajo difie-
re ampliamente entre quienes tienen el título de CFGM y quienes no han
obtenido el título de GESO, puesto que es más favorable para el primer
grupo, en tanto participa en mayor grado en el empleo, tiene menos periodos
de paro y de no participación en el mundo laboral ni en la educación. En
ambos grupos, las mujeres —respecto a los hombres— presentan menor dedi-
cación al mundo productivo, están desempleadas en mayor grado o se
encuentran sin buscar trabajo.
    """)  # Respuesta: Educación 2 FALLA en realzar la semántica, ya que el texto es exactamente el mismo del de un doc.

# TODO
# 1) Formatear y FINALIZAR el proyecto con tf-idf por palabra, incluyendo sufijos y plurales
# 2) Investigar diferentes formas de similitud y/o mejoras del tf-idf (2+ términos)
# 3) Ver factibilidad de 2) e implementar dado el caso
