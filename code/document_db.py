import sys

import create
import search


def invalido():
    print("invalid command")
    exit()


if len(sys.argv) != 3:
    invalido()

if sys.argv[1] == "-create":
    create.create(sys.argv[2])
elif sys.argv == "-search":
    search.search(sys.argv[2])
else:
    invalido()
