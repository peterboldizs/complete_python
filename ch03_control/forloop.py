#!/usr/bin/python3
from datetime import date, timedelta
from itertools import count, permutations

print("for loop")
for j in range(1, 20, 4):
    print("j=", j)

names = ['peter', 'marti', 'david', 'dori', 'anna']
ages = [47, 46, 17, 16, 11]
for pos in range(len(names)):
    # print(pos, names[pos][0])
    print(pos, names[pos], ages[pos])

for pos, name in enumerate(names):
    age = ages[pos]
    print(pos, name, age)

for name, age in zip(names, ages):
    print(name, age)

for data in zip(names, ages):
    name, age = data
    print(name, age)

print("***discount")
today = date.today()
tomorrow = today + timedelta(days=1)
prods = [
    {'id': 1, 'exp': today, 'price': 100.0},
    {'id': 2, 'exp': tomorrow, 'price': 1000.0},
    {'id': 3, 'exp': today, 'price': 80.0},
    {'id': 4, 'exp': tomorrow, 'price': 70.0}
]
for prod in prods:
    print("checking id ", prod['id'], "...")
    if prod['exp'] != today:
        continue
    prod['price'] *= 0.8
    print("price for ", prod['id'], ' is now ', prod['price'])

found = False
for pr2 in prods:
    print("checking id ", pr2['id'], "...")
    if pr2['id'] == 3:
        found = True
        print("id: ", pr2['id'])
        break

if found:
    print("found it!")
else:
    print("no luck...")


class OldException(Exception):
    pass


# old = None
for data in zip(names, ages):
    name, age = data
    if age > 40:
        old = name
        print("old found: ", name, age)
        break
# if old is None:
else:
    raise OldException("nobody found")

print("primes")
primes = []
upto = 50
for n in range(2, upto + 1):
    # is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            # is_prime = False
            break
    # if is_prime:
    else:
        primes.append(n)
print(primes)

print("discounts")
customers = [
    dict(id=1, total=200, c_c='f20'),
    dict(id=2, total=2000, c_c='p20'),
    dict(id=3, total=200, c_c='f40'),
    dict(id=4, total=500, c_c='p40'),
]
discount = {
    'f20': (0.0, 20.0),
    'f40': (0.0, 40.0),
    'p20': (0.20, 0.0),
    'p40': (0.40, 0.0),
}

for cust in customers:
    code = cust['c_c']
    percent, fixed = discount.get(code, (0.0, 0.0))
    cust['discount'] = percent * cust['total'] + fixed
    print(cust['id'], cust['total'], cust['discount'])

# for c in customers:
#     print(c['id'], c['total'], c['discount'])

for n in count(5,2):
    if n > 20:
        break
    print(n, end=', ')

print("permutations")
print(list(permutations('ABC')))