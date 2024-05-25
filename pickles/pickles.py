import os
import pickle

PATH = "/home/admin1/Documents/Universidad/2do/Algoritmos2/proyecto-algo2/pickles"


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
