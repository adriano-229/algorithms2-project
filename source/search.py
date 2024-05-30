from create import DB_FILENAMES, DB_TF_LIST, DB_MAIN_EMPTY_VEC
from formatting import remove_keys, associate_names, sort_present_dicc
from parsing import *
from pickles import pickle_load
from similitude import compare_cosine_similarity


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

    create_vectors = remove_keys(tfidf_vec_list)
    search_vector = create_vectors.pop()
    del corpus_size, idf, main_empty_vec, search_tf, text, tf_list, tfidf_vec_list

    compare = compare_cosine_similarity(create_vectors, search_vector)
    result = associate_names(filenames, compare)
    result = sort_present_dicc(result)
    return result


if __name__ == "__main__":
    search("""
    La Mixteca Alta Oaxaqueña, México (MAO), presenta niveles
moderados a graves de degradación de suelo. La erosión hídri-
ca y eólica son las principales causas de esa degradación, con
pérdidas de suelo entre 50 y 200 Mg ha-1 año-1 y en algunas
zonas puede ser mayor. Los indicadores de calidad (ICS) son
herramientas útiles para evaluar el estado de la fertilidad del
suelo y su degradación. El objetivo de este estudio fue generar
indicadores de calidad (univariados) cuyos valores, compren-
didos dentro de una escala única, permitan evaluar la fertili-
dad de suelos de la MAO y situarlos en un mapa temático de
degradación. Las hipótesis fueron: 1) los atributos evaluados
en este estudio funcionan como ICS y 2) los valores de los
ICS que varían dentro de una escala única permiten compa-
rar los estados de estos atributos. El valor de los indicadores
permitirá proponer acciones correctivas del manejo agronó-
mico de los suelos y evitar su degradación. Esta propuesta es
de ejecución fácil, costo bajo, generación rápida, que usa in-
formación disponible en la literatura y puede apoyar políticas
públicas regionales. Los atributos químicos y fisicoquímicos
evaluados fueron: pH, materia orgánica (MO), P extraíble
(Pex), bases de intercambio (Ca, Mg y K), capacidad de inter-
cambio catiónico efectiva (CICE); además, uno biológico, el
carbono en biomasa microbiana (CBM). Con estos atributos
se definieron los indicadores de calidad, los valores de éstos y
las clases de calidad de suelo en sitios agrícolas y degradados
de cinco localidades de la MAO: Tonaltepec, Gavillera, Cerro
Prieto, Nduayaco y Pericón, donde hubo apoyo de la comu-
nidad. El muestreo fue completamente aleatorio. Los sitios
de donde se obtuvieron las muestras para generar los ICS se
georeferenciaron y ubicaron en un mapa temático de tipos de
degradación.
    """)
    # Respuesta: Agrociencia -> FALLA en realzar la semántica, ya que el texto es exactamente el mismo del de un doc.

# TODO
# 1) Formatear y FINALIZAR el proyecto con tf-idf por palabra, incluyendo sufijos y plurales
# 2) Investigar diferentes formas de similitud y/o mejoras del tf-idf (2+ términos)
# 3) Ver factibilidad de 2) e implementar dado el caso
