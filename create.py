from categorization.parsing import *
from pickles import pickles

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
    tf_list = calculate_term_frequencies(word_lists)

    idf = calculate_inverse_document_frequencies(tf_list)
    
    pickles.pickle_dump(idf, "DB_IDF_LIST")
    pickles.pickle_dump(list(filenames), "FILENAMES")
    pickles.pickle_dump(tf_list, "DB_TF_LIST")
    print("document data-base created successfully")
