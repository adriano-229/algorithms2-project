import math
from categorization.parsing import *
from pickles.pickles import *
from categorization.similitude import cosine_similarity

def search(text):
    DB_TF_LIST = pickle_load("DB_TF_LIST")
    DB_IDF_LIST = pickle_load("DB_IDF_LIST")
    FILENAMES = pickle_load("FILENAMES")
    #DB_MAIN_EMPTY_VEC = pickle_load("FILENAME_DB_MAIN_EMPTY_VEC")
    word_list = create_word_lists_from_texts([text])

    search_tf = calculate_term_frequencies(word_list)
    DB_TF_LIST += search_tf

    for word in word_list[0]:
        DB_IDF_LIST[word] = DB_IDF_LIST.get(word,0) + 1
    for word in DB_IDF_LIST.keys():
        DB_IDF_LIST[word] = math.log2(len(DB_TF_LIST) / DB_IDF_LIST[word])

    tfidf_vec_lists = calculate_tfidf_vectors(DB_TF_LIST, DB_IDF_LIST)

    ranked = {}
    for i in range(len(tfidf_vec_lists)-1):
        ranked[FILENAMES[i]] = cosine_similarity(tfidf_vec_lists[-1],tfidf_vec_lists[i])

    rankedOrd = {k: v for k, v in sorted(ranked.items(), key=lambda item: item[1], reverse = True)}

    count = 0
    for k in rankedOrd.keys():
        count += 1
        print(f"{count}. {k}")
"""
if __name__ == "__main__":
    search("abcdefghijklmnopqrst hola messi asado tenis perro perro perro perro")
"""