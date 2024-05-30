import os
import sys

import create
import search
from globals import PICKLES_DUMP_PATH, DB_FILENAMES, DB_MAIN_EMPTY_VEC


def rewrite_db():
    try:
        open(os.path.join(PICKLES_DUMP_PATH, DB_FILENAMES))
        open(os.path.join(PICKLES_DUMP_PATH, DB_MAIN_EMPTY_VEC))
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


def invalid():
    quit("invalid command")


if len(sys.argv) != 3:
    invalid()

if sys.argv[1] == "-create":
    create.create(sys.argv[2])
elif sys.argv == "-search":
    search.search(sys.argv[2])
else:
    invalid()
