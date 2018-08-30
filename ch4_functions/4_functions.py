#!/usr/bin/python3
from functools import reduce
from operator import mul
from math import ceil, sqrt

import sys
import builtins

print("functions")


def my_func():
    test = 1
    print("myfunc: ", test)

test = 0
my_func()

def outer():
    test = 3
    print("outer", test)

    def inner():
        nonlocal test
        test = 4
        print("inner", test)
    inner()

outer()
print("global: ", test)

x = [1,2,3]
print("x list before: ", x)


def func1(x):
    x[1] = 42
    x = 'something'
    print("local x: ", x)

func1(x)
print("x list after", x)


def pos_func(x,y,z):
    print(x, y, z)

pos_func(1, 2, 3)
pos_func(x=1, z=2, y=3)


def pos_func2(x, y, z=44):
    print(x, y, z)

pos_func2(1,2)
pos_func2(1, 2, 88)
# pos_func2(y=3, z=3, 44) SyntaxError: positional argument follows keyword argument


def minimum(*n):
    print(n)
    if n:
        mn = n[0]
        for val in n[1:]:
            if val < mn:
                mn = val
        print("minimum: ", mn)

minimum(1, 2, 36, -9, -7)

def func2(*args):
    print(args)

values = (1,2,3,4,5)
func2(values)
func2(*values) # unpacking


def func3(**kwargs):
    print(kwargs)

func3(a=1, b=2)
func3(**dict(a=1, b=2))


def func_args(a, b, c=7, *args, **kwargs):
    print('a,b,c: ', a,b,c)
    print('args: ', args)
    print('kwargs: ', kwargs)

func_args(1, 2, 3, *(5,7,9), **{'d': 10, 'e': 11})
func_args(11, 12, *(15,17,19), **{'d': 20, 'e': 21})


def func_none():
    pass

a = func_none()
print(a)


def ffactorial(n):
    if n in (0,1):
        return 1
    result = n
    for k in range(2,n):
        result *= k
    return result

f5 = ffactorial(5)
print(f5)


def fact2(n):
    return reduce(mul, range(1, n+1), 1)

f6 = fact2(6)
print("reduce fact: ",f6)


def mod_div(a, b):
    return a // b, a % b

print("mod_div: ", mod_div(20, 7))

numbers = [1,4,5,2]
print("orig: ", numbers)
ns = sorted(numbers)
print("after sorted: ", numbers)
numbers.sort()
print("sort: ", numbers)


def rec_fact(n):
    if n in (0,1):
        return 1
    return rec_fact(n -1) * n

print("rec_fact: ", rec_fact(5))

print("sys.getrecursionlimit(): ", sys.getrecursionlimit())


def mult_five(n):
    return list(filter(lambda k: not k % 5, range(n)))

print(mult_five(50))

# for b in dir(builtins):
#    print(b)


def get_primes(n):
    """calculates list of primes."""
    primes = []
    for num in range(2, n+1):
        is_prime = True
        root = int(ceil(sqrt(num)))
        for prime in primes:
            if prime > root:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print("primes: ", get_primes(50))