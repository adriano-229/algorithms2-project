from categorization.parsing import *
from globals import DB_FILENAMES, DB_TF_LIST, DB_MAIN_EMPTY_VEC, PDF_FOLDER_PATH
from pickles import pickle_dump


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

    # if not rewrite_db():
    #     return

    corpus_pdfs_str = create_texts_from_pdfs(path)
    filenames, texts = list(corpus_pdfs_str.keys()), corpus_pdfs_str.values()

    word_lists = create_word_lists_from_texts(texts)
    main_empty_vec = create_main_vector(word_lists)
    tf_list = calculate_term_frequencies(word_lists, main_empty_vec)
    del path, corpus_pdfs_str, word_lists

    dump = {
        DB_FILENAMES: filenames,
        DB_TF_LIST: tf_list,
        DB_MAIN_EMPTY_VEC: main_empty_vec
    }
    for var, name in dump.items():
        pickle_dump(name, var)

    print("document data-base created successfully")
    return


if __name__ == "__main__":
    create(PDF_FOLDER_PATH)
