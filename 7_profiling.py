#!/usr/bin/python3
import sys
#from math import sqrt

num = int(sys.argv[1])
mode = int(sys.argv[2])

def calc_triples(mx):
    triples = []
    for a in range(1, mx +1):
        for b in range(a, mx +1):
            if mode == 1:
                hypo = calc_hypo(a, b)
            elif mode == 2:
                hypo = calc_hypo2(a, b)
#           elif mode == 3:
#              hypo = calc_hypo3(a, b)
            else:
                hypo = calc_hypo(a, b)

            if is_int(hypo):
                triples.append((a, b, int(hypo)))
    return triples


def calc_hypo(a, b):
    return (a ** 2 + b ** 2) ** 0.5


def calc_hypo2(a, b):
    return (a * a + b * b) ** 0.5


#def calc_hypo3(a, b):
#    return sqrt(a * a + b * b)


def is_int(n):
    return n.is_integer()

triplelist = calc_triples(num)
# print(triplelist)