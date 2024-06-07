from parsing import *
from pickles_ import *


def create(path):
    if not os.path.isdir(path):
        raise Exception("The provided path is not a directory")

    corpus_pdfs_str = create_texts_from_pdfs(path)
    filenames, texts = corpus_pdfs_str.keys(), corpus_pdfs_str.values()

    word_lists = create_word_lists_from_texts(texts)
    tf_list = calculate_term_frequencies(word_lists)
    idf = calculate_document_occurrences(tf_list)

    dump = {
        DB_FILENAMES: list(filenames),
        DB_TF_LIST: tf_list,
        DB_IDF: idf
    }
    for name, content in dump.items():
        pickle_dump(content, name)

    print("document data-base created successfully")
    return


if __name__ == "__main__":
    create("/home/admin1/Documents/Universidad/2do/Algoritmos2/proyecto-algo2/pdfs")
