names = ["Peter", "Marti", "David", "Dori", "Anna"]
with open("names.txt", 'w') as name_file:
    for n in names:
        print(n, file=name_file)

print("*" * 40)
print("read from file - newline stripped")
names2 = []
with open("names.txt", 'r') as name_file2:
    for n in name_file2:
        names2.append(n.strip('\n'))
print(names2)

for n in names2:
    print(n)

print("Adelaide".strip("del"))
print("*" * 40)
print("read write tuples")
person = ("Peter", "Boldizs", 1970)
person2 = (person, ((1, "Astra F", 1997), (2, "Vectra B", 2002), (3, "Astra K", 2018)))
with open("person.txt", 'w') as person_file:
    print(person2, file=person_file)

with open("person.txt", 'r') as person_file:
    p = person_file.readline()

pers2 = eval(p)
print(pers2)
fname, lname, year = pers2[0]
id, model, myear = pers2[1][1]
print("person: {} {} {}".format(fname, lname, year))
print("car: {} {} {}".format(id, model, myear))

print("*" * 40)
print("append to file")
with open("names.txt", 'a') as name_file3:
    for i in range(1, 6):
        for j in range(1,6):
            print("{} * {} = {}".format(i, j, i * j), file=name_file3)
        print("-" * 20, file=name_file3)
