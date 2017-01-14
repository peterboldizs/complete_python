#!/usr/bin/python3

def try_syntax(num, dom):
    try:
        print("In try block: {0}/{1}".format(num, dom))
        res = num / dom
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print("Result: {0}".format(res))
        return res
    finally:
        print("exiting")


print(try_syntax(4, 2))
print(try_syntax(4, 0))

class ExitLoopException(Exception):
    pass

def find_roots():
    try:
        n = 100
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    if 42 * a + 17 * b + c == 5096:
                        raise ExitLoopException(a, b, c)
    except ExitLoopException as ele:
        print(ele)

print("find roots")
find_roots()
