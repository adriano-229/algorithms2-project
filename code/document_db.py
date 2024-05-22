import sys

import create
import search


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
