from categorization.parsing import *
from pickles import *

FILENAME_DB_TF_LIST = "DB_TF_LIST"
FILENAME_DB_MAIN_EMPTY_VEC = "DB_MAIN_EMPTY_VEC"


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

    # try:
    #     open(os.path.join(PATH, FILENAME_DB_TF_LIST))
    #     open(os.path.join(PATH, FILENAME_DB_MAIN_EMPTY_VEC))
    #     if not bool(input("DB exists, rewrite existing DB? Press 1 YES or ENTER NO: ")):
    #         print("Finished")
    #         return
    # except:
    #     if not bool(input("No existing DB, want to create? Press 1 YES or ENTER NO: ")):
    #         print("No db created, quiting")
    #         return
    #     else:
    #         pass

    corpus_pdfs_str = create_texts_from_pdfs(path)
    filenames = corpus_pdfs_str.keys()  # TODO, asociar nombres a resultados

    word_lists = create_word_lists_from_texts(corpus_pdfs_str.values())
    main_empty_vec = create_main_vector(word_lists)
    tf_list = calculate_term_frequencies(word_lists, main_empty_vec)

    # idf = calculate_inverse_document_frequencies(main_empty_vec, tf_list, len(corpus_pdfs_str))
    # tfidf_vec_list = calculate_tfidf_vectors(tf_list, idf)
    # print(cosine_similarity(list(tfidf_vec_list[2].values()), list(tfidf_vec_list[1].values())))

    pickle_dump(tf_list, FILENAME_DB_TF_LIST)
    pickle_dump(main_empty_vec, FILENAME_DB_MAIN_EMPTY_VEC)
    print("document data-base created successfully")


if __name__ == "__main__":
    create("/home/admin1/Documents/Universidad/2do/Algoritmos 2/proyecto-algo2/pdfs/simple")
