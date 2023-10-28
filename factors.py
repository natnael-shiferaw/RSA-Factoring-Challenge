#!/usr/bin/python3


from sys import argv
import math
"""THIS FILE IS USED TO FACTORIZE AS MANY NUMBERS
AS POSSIBLE AS A PRODUCT OF TWO SMALL NUMBERS."""


def FACTORY(num):
    """FUNCTION USED TO GET the FACTORS of a NUMBER."""

    if num % 2 == 0:
        j = 2
        print("{}={}*{}".format(num, int(num//j), j))

    else:
        sq = int(math.sqrt(num)) + 1

        for j in range(3, sq, +2):
            if num % j == 0:
                print("{}={}*{}".format(num, int(num//j), j))
                return
            if num % (sq + j) == 0:
                print("{}={}*{}".format(num, sq + j, int(num//(sq + j))))
                return
            if num % (sq - j) == 0:
                print("{}={}*{}".format(num, sq - 1, int(num//(sq - j))))
                return


def FACTORS(FILE_NAME):
    """A FUNCTION USED TO READ AND PRINT A FILE."""

    with open(FILE_NAME, encoding="utf-8") as my_file:

        for j in my_file.readlines():
            k = int(j)
            result = FACTORY(k)


if __name__ == "__main__":
    FACTORS(argv[1])
