a = 2
b = 3
print("a = {}, b = {}".format(a, b))

a, b = b, a
print("a = {}, b = {}".format(a, b))


def fibonacci():
    cur, prev = 0, 1
    while True:
        yield cur
        cur, prev = cur + prev, cur


def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


print("fibonacci")
fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

print("pi calculation")


def calc_pi():
    odd = odd_numbers()
    approx = 0
    while True:
        approx += (4 / next(odd))
        yield approx
        approx -= (4 / next(odd))
        yield approx


approx_pi = calc_pi()
for x in range(50):  # 10 million iterations would be accurate enough
    print(next(approx_pi))
