from itertools import count, permutations

print("calculations using for loop")
print("primes")
primes = []
upto = 30
for n in range(2, upto + 1):
    # is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            # is_prime = False
            break
    else:  # if is_prime - it executes only if there was no break
        primes.append(n)
print(primes)

print("discounts")

discount = {
    'f20': (0.0, 20.0),
    'f40': (0.0, 40.0),
    'p20': (0.20, 0.0),
    'p40': (0.40, 0.0),
}

customers = [
    dict(id=1, total=200, c_c='f20'),
    dict(id=2, total=2000, c_c='p20'),
    dict(id=3, total=200, c_c='f40'),
    dict(id=4, total=500, c_c='p40'),
]

for cust in customers:
    code = cust['c_c']
    percent, fixed = discount.get(code, (0.0, 0.0))
    cust['discount'] = percent * cust['total'] + fixed
    print(cust['id'], cust['total'], cust['discount'])

for n in count(5, 2):
    if n > 20:
        break
    print(n, end=', ')

print("\npermutations")
print(list(permutations('ABC')))
