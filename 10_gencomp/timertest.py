import timeit
from statistics import mean, stdev

print("multiplication table 1")
multi1 = """\
for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i *j))
"""

print("-" * 40)
print("multiplication table 2")
multi2 = """\
m_table = [(i, j, i * j) for i in range(1, 11) for j in range(1, 11)]
print(m_table)
"""


def f_multi1_print():
    for i in range(1, 51):
        for j in range(1, 51):
            print("{} * {} = {}".format(i, j, i * j))


def f_multi1_noprint():
    res = []
    for i in range(1, 51):
        for j in range(1, 51):
            res.append((i, j, i * j))
    return res


def f_multi_compre():
    m_table = [(i, j, i * j) for i in range(1, 51) for j in range(1, 51)]
    return m_table


def f_multi_gener():
    m_table = ((i, j, i * j) for i in range(1, 51) for j in range(1, 51))
    return m_table


def iterative_factorial(n):
    result = 1
    if n > 1:
        for j in range(2, n + 1):
            result *= j
    return result


def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


# strings
# res_multi1 = timeit.timeit(multi1, globals=globals(), number=100)
# res_multi2 = timeit.timeit(multi2, number=100)

# functions
# res_f_multi1_print = timeit.timeit(f_multi1_print, number=100)
res_f_multi1_noprint = timeit.timeit(f_multi1_noprint, number=1000)
res_f_multi_compre = timeit.timeit(f_multi_compre, number=1000)
res_f_multi_gener = timeit.timeit(f_multi_gener, number=1000)

print("iterative: {}".format(iterative_factorial(10)))
print("recursive: {}".format(recursive_factorial(10)))

# print("res_multi1: {}".format(res_multi1))
# print("res_multi2: {}".format(res_multi2))
# print("res_f_multi1_print: {}".format(res_f_multi1_print))
print("res_f_multi1_noprint: {}".format(res_f_multi1_noprint))
print("res_f_multi_compre: {}".format(res_f_multi_compre))
print("res_f_multi_gener: {}".format(res_f_multi_gener))

# print("res_iterative_factorial: {}".format(res_iterative_factorial))
# print("res_recursive_factorial: {}".format(res_recursive_factorial))

# it only executes when run as a script
if __name__ == "__main__":
    print(timeit.timeit("x = iterative_factorial(20)", setup="from __main__ import iterative_factorial", number=1000))
    print(timeit.timeit("x = recursive_factorial(20)", setup="from __main__ import recursive_factorial", number=1000))
    listiter = timeit.repeat("x = iterative_factorial(20)", setup="from __main__ import iterative_factorial",
                             number=1000, repeat=5)
    listrecur = timeit.repeat("x = recursive_factorial(20)", setup="from __main__ import recursive_factorial",
                              number=1000, repeat=5)
    print("iter: mean: {}, std dev: {}".format(mean(listiter), stdev(listiter)))
    print("recur: mean: {}, std dev: {}".format(mean(listrecur), stdev(listrecur)))
