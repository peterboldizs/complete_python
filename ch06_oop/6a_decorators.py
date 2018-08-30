#!/usr/bin/python3

from time import time, sleep
from functools import wraps

print("basic function")
def f(sleep_time=0.1):
    sleep(sleep_time)

def measure1(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "took ", time() - t, " seconds")

measure1(f, 0.8)

print("decorator function")
def measure2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, "took ", time() - t, " seconds")
        return result
    return wrapper

@measure2
def f2(sl=0.1):
    """This is a sleeper function"""
    sleep(sl)

f2(1.0)
print(f2.__name__, f2.__doc__)

def max_res(limit):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if res > limit:
                print("Result is too big: {0} - max is {1}".format(res, limit))
            return res
        return wrapper
    return decorator

# @measure2
@max_res(100)
def cube(n):
    return n ** 3

@max_res(60)
def square(n):
    return n ** 2


print(cube(3))
print(cube(8))
print(square(8))
print(square(6))