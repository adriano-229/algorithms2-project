from parsing import *
from pickles import *


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

    corpus_pdfs_str = create_texts_from_pdfs(path)
    all_word_lists = create_word_lists_from_texts(corpus_pdfs_str)
    main_empty_vec = create_main_vector(all_word_lists)
    tf_list = calculate_term_frequencies(all_word_lists, main_empty_vec)
    # idf = calculate_inverse_document_frequencies(main_empty_vec, tf_list, len(corpus_pdfs_str))
    # tfidf_vec_list = calculate_tfidf_vectors(tf_list, idf)

    pickle_dump(tf_list, "tf_list")
    pickle_dump(main_empty_vec, "main_empty_vec")
    print("document data-base created successfully")


if __name__ == "__main__":
    create(
        "/home/admin1/Documents/Universidad/2do/Algoritmos 2/proyecto-algo2/code/test_pdfs")
