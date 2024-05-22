import pickle


def pickle_dump(file, name):
    with open(name, 'bw') as f:
        pickle.dump(file, f)
    return


def pickle_load(name):
    with open(name, 'br') as file:
        ld = pickle.load(file)
    return ld
