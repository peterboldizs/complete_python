import sys

print("program to test exceptions")


def factorial(n):
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n - 1)


def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("invalid number, try again")
        except EOFError:
            print("exiting...")
            sys.exit(1)


try:
    print(factorial(get_int("enter num to fact")))
except RecursionError:
    print("number too large")

print("division")
first = get_int("enter first")
second = get_int("enter second")

try:
    res = first / second
    print("{} divided by {} is {}".format(first, second, res))
except ZeroDivisionError:
    print("you should not divide by zero")
    sys.exit(2)
finally:
    print("finally always runs")
