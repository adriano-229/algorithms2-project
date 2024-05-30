import os
import pickle

PATH = "pickles"


def pickle_dump(file, name): #Guarda el archivo
    path = os.path.join(PATH, name)
    with open(path, 'bw') as f:
        pickle.dump(file, f)
    return


def pickle_load(name): #Levanta el archivo
    path = os.path.join(PATH, name)
    with open(path, 'br') as file:
        ld = pickle.load(file)
    return ld
