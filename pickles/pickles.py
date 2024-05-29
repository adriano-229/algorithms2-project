import os
import pickle

PATH = "C://Users//renzo//Desktop//Algoritmos2//Proyecto//proyecto-algo2-1//pickles"


def pickle_dump(file, name):
    path = os.path.join(PATH, name)
    with open(path, 'bw') as f:
        pickle.dump(file, f)
    return


def pickle_load(name):
    path = os.path.join(PATH, name)
    with open(path, 'br') as file:
        ld = pickle.load(file)
    return ld
