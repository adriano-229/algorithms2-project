import pickle

DB_FILENAMES = "DB_FILENAMES.pkl"
DB_TF_LIST = "DB_TF_LIST.pkl"
DB_IDF = "DB_IDF.pkl"


def pickle_dump(to_save, name):
    with open(name, 'bw') as f:
        pickle.dump(to_save, f)
    return None


def pickle_load(name):
    with open(name, 'br') as file:
        ld = pickle.load(file)
    return ld
