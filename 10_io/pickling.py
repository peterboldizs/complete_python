import pickle

print("writing to pickle")
person = ("Peter", "Boldizs", 1970)
person2 = (person,
           ((1, "Astra F", 1997),
            (2, "Vectra B", 2002),
            (3, "Astra K", 2018)))
with open("person2.pickle", 'wb') as pickle_file:
    pickle.dump(person2, pickle_file)

print("-" * 40)
print("reading from pickle")
with open("person2.pickle", 'rb') as pickled_person:
    person3 = pickle.load(pickled_person)
    print(person3)

fname, lname, year = person3[0]
print("person: {} {} {}".format(fname, lname, year))
car = person3[1]
for i in range(len(car)):
    id, model, myear = car[i]
    print("car {}: {} {}".format(id, model, myear))

print("-" * 40)
print("reading more items from pickle")
odd = list(range(1, 10, 2))
even = list(range(0, 10, 2))
with open("person3.pickle", 'wb') as pickle_file2:
    pickle.dump(person2, pickle_file2, protocol=0)
    pickle.dump(odd, pickle_file2, protocol=0)
    pickle.dump(even, pickle_file2, protocol=0)

with open("person3.pickle", 'rb') as pickled_things:
    person3 = pickle.load(pickled_things)
    print(person3)
    odd_list = pickle.load(pickled_things)
    print(odd_list)
    even_list = pickle.load(pickled_things)
    print(even_list)
