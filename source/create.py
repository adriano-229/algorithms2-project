from categorization.parsing import *
from pickles import *

DB_FILENAMES = "DB_FILENAMES"
DB_TF_LIST = "DB_TF_LIST"
DB_MAIN_EMPTY_VEC = "DB_MAIN_EMPTY_VEC"


def rewrite_db():
    try:
        open(os.path.join(PATH, DB_FILENAMES))
        open(os.path.join(PATH, DB_MAIN_EMPTY_VEC))
        rewrite = bool(input("DB exists, rewrite DB? Press 1 YES or ENTER NO: "))
        if not rewrite:
            print("using created DB")
            print("document data-base created successfully")
        return rewrite

    except:
        create = bool(input("Nonexistent DB, create DB? Press 1 YES or ENTER NO: "))
        if not create:
            quit("quiting program")
        return create


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

    if not rewrite_db():
        return

    corpus_pdfs_str = create_texts_from_pdfs(path)
    filenames, texts = list(corpus_pdfs_str.keys()), corpus_pdfs_str.values()

    word_lists = create_word_lists_from_texts(texts)
    main_empty_vec = create_main_vector(word_lists)
    tf_list = calculate_term_frequencies(word_lists, main_empty_vec)
    del path, corpus_pdfs_str, word_lists

    pickle_dump(filenames, DB_FILENAMES)
    pickle_dump(tf_list, DB_TF_LIST)
    pickle_dump(main_empty_vec, DB_MAIN_EMPTY_VEC)
    print("document data-base created successfully")


if __name__ == "__main__":
    create("/home/admin1/Documents/Universidad/2do/Algoritmos2/proyecto-algo2/pdfs/complex")
