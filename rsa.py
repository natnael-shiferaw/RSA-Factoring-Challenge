#!/usr/bin/python3

from sys import argv
import math

"""THIS FILE IS USED TO GET the FIRST TWO FACTORS OF A GIVEN NUMBER."""


def IS_PRIME(num):
    """A FUNCTION USED TO CHECK if a NUMBER is PRIME."""

    k = 3

    if num % 2 == 0:
        return False

    while k * k <= num:
        if num % k == 0:
            return False
        k += 2
    return True


def FACTORY(num):
    """THIS FUNCTION IS USED TO GET AND PRINT THE FACTORS OF A GIVEN NUMBER."""

    if num % 2 == 0:
        k = 2
        print("{}={}*{}".format(num, int(num/k), k))

    else:
        sq = math.sqrt(num)

        if sq % 1 == 0:
            print("{}={}*{}".format(num, sq, int(num/sq)))
            return
        sq = int(sq) + 1

        for k in range(3, sq, +2):

            if num % k == 0:
                if IS_PRIME(k):
                    print("{}={}*{}".format(num, int(num/k), k))
                    return


def FACTORS(FILE_NAME):
    """THIS FUNCTION IS USED TO READ A FILE."""

    with open(FILE_NAME, encoding="utf-8") as MYfile:

        for j in MYfile.readlines():
            S = int(j)
            result = FACTORY(S)


if __name__ == "__main__":
    FACTORS(argv[1])
