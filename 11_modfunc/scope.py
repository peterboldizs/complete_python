def fact(n):
    result = 1
    if n > 1:
        for j in range(2, n + 1):
            result *= j
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_1 = 1
        n_2 = 0
        for f in range(1, n):
            result = n_1 + n_2
            n_2 = n_1
            n_1 = result
    return result


print("iterative factorial")
for i in range(10):
    print("{}! is {}".format(i, fact(i)))

print("recursive factorial")
for k in range(10):
    print("{}! is {}".format(k, factorial(k)))

print("recursive fibonacci")
# much slower
for l in range(20):
    print(fibo(l), end=' ')

print("\niterative fibonacci")
for m in range(20):
    print(fibonacci(m), end=' ')
