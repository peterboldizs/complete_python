print("tuples")
my_tu = 1, "A", 12.5, 'Peter'
print(my_tu)
print(my_tu[2])
#my_tu[1] = 3  TypeError: 'tuple' object does not support item assignment 
person = ("Peter", "Boldizs", 1970)
first, last, year = person

print("unpacking")
print("first name: {}".format(first))
print("last name: {}".format(last))
print("birth: {}".format(year))

print("extending the existing tuple")
person2 = (person, ((1, "Astra F", 1997), (2, "Vectra B", 2002), (3, "Astra K", 2018)))
num_cars = len(person2[0])
print("{} cars of {} {}:".format(num_cars, person2[0][1], person2[0][0]))
for car in person2[1]:
    # another level of unpacking
    id, model, year = car
    print("Car ID: {} - Model: {} - Year {}".format(id, model, year))

print("lists in tuples")
person3 = (person, [(1, "Astra F", 1997), (2, "Vectra B", 2002), (3, "Astra K", 2018)])
person3[1].append((4, "Suzuki", 1993))
for car in person3[1]:
    id, model, year = car
    print("Car ID: {} - Model: {} - Year {}".format(id, model, year))
