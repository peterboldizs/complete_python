from datetime import date, timedelta

print("advanced for")
names = ['peter', 'marti', 'david', 'dori', 'anna']
ages = [47, 46, 17, 16, 11]

print("\nprint arrays")
for pos in range(len(names)):
    # print(pos, names[pos][0])
    print(pos, names[pos], ages[pos] + 1)

print("\nprint enumerate")
for pos, name in enumerate(names):
    age = ages[pos]
    print(pos, name, age)

print("\nprint zip 1")
for name, age in zip(names, ages):
    print(name, age)

print("\nprint zip 2")
for data in zip(names, ages):
    name, age = data
    print(name, age)

print("\nbreak and continue")
print("discount")
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

for name in names:
    if name == "peter":
        print("Ignoring {}".format(name))
        continue
    print(name)

numbers = "234,567,789,765.765"
cleanCharset = ''
for ch in numbers:
    if ch in ",":
        continue
    cleanCharset = cleanCharset + ch

print("cleaned character set: {}".format(cleanCharset))

for data in zip(names, ages):
    name, age = data
    if age > 40:
        old = name
        print("old found: ", name, age)
        continue

for data in zip(names, ages):
    name, age = data
    if age <= 18:
        young = name
        print("young found: ", name, age)
        break
