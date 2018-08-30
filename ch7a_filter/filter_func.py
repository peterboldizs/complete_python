#!/usr/bin/python3


def is_positive(num):
    return num > 0


def filter_ints(v):
    return [num for num in v if is_positive(num)]
