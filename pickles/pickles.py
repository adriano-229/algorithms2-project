import os
import pickle

from globals import PICKLES_DUMP_PATH


def pickle_dump(file, name):
    path = os.path.join(PICKLES_DUMP_PATH, name)
    with open(path, 'bw') as f:
        pickle.dump(file, f)
    return


def pickle_load(name):
    path = os.path.join(PICKLES_DUMP_PATH, name)
    with open(path, 'br') as file:
        ld = pickle.load(file)
    return ld
