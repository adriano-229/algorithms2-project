import sys

import search
import create



def invalid():
    quit("Invalid command.")


if len(sys.argv) != 3:
    invalid()

if sys.argv[1] == "-create":
    create.create(sys.argv[2])
elif sys.argv[1] == "-search":
    search.search(sys.argv[2])
else:
    invalid()
