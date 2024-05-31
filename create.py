from parsing import *
from pickles_ import *


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

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
    for name, content in dump.items():
        pickle_dump(content, name)

    print("document data-base created successfully")
    return
