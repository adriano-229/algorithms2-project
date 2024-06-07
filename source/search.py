import math

from formatting import associate_names, sort_show_dicc
from parsing import *
from pickles_ import *
from similitude import compare_with_cosine_similarity


def search(text):
    if not text:
        print("document not found")
        return

    db_filenames = pickle_load(DB_FILENAMES)
    db_tf_list = pickle_load(DB_TF_LIST)
    db_idf = pickle_load(DB_IDF)
    corpus_size = len(db_tf_list) + 1

    word_list = create_word_lists_from_texts([text])
    search_tf = calculate_term_frequencies(word_list)
    db_tf_list += search_tf

    for word in word_list[0]:
        db_idf[word] = db_idf.get(word, 1) + 1
    for word in db_idf.keys():
        db_idf[word] = math.log2(corpus_size / db_idf[word])

    tfidf = calculate_tfidf_vectors(db_tf_list, db_idf)
    search_vector = tfidf.pop()

    compare = compare_with_cosine_similarity(tfidf, search_vector)
    result = associate_names(db_filenames, compare)

    if not sort_show_dicc(result):
        print("document not found")
    return


if __name__ == "__main__":
    search("""
    La Mixteca Alta Oaxaqueña, México (MAO), presenta niveles
moderados a graves de degradación de suelo.
    """)
