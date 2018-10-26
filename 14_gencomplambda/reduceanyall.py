import functools

numbers = [1, 2, 3, 4, 5]


def calc_sum(x, y: int):
    return x + y


def calc_mul(x, y: int):
    return x * y


summa = functools.reduce(calc_sum, numbers)
print("summa: {}".format(summa))

# how it works:
res = calc_sum(1, 2)
res = calc_sum(res, 3)
res = calc_sum(res, 4)
res = calc_sum(res, 5)
print("res_sum: {}".format(res))

mul = functools.reduce(calc_mul, numbers)
print("mul: {}".format(mul))

res = calc_mul(1, 2)
res = calc_mul(res, 3)
res = calc_mul(res, 4)
res = calc_mul(res, 5)
print("res_mul: {}".format(res))

numbers_zero = [1, 2, 3, 0, 4, 5, 0]
empty_list = []

print("any: {}".format(any(numbers)))
print("all: {}".format(all(numbers)))
print("zero any: {}".format(any(numbers_zero)))
print("zero all: {}".format(all(numbers_zero)))
print("empty any: {}".format(any(empty_list)))
print("empty all: {}".format(all(empty_list)))
