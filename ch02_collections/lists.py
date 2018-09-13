print("All about lists")
le1 = []
le2 = list()
le3 = le1
print("my empty lists: {} and {}".format(le1, le2))
print("le1 is le2: {}".format(le1 is le2))
print("le1 == le2: {}".format(le1 == le2))  # contents are equal
print("le1 is le3: {}".format(le1 is le3))
my_string = "This is my string"
my_list0 = list(my_string)
print(my_list0)

my_list = [1, 2, 3]
for x in my_list:
    print(x)

for x in my_list:
    print(x, end='')

print("\noperating on list items:")
print([x + 5 for x in my_list])

print("appending and extending")
my_list.append(12)
my_list.extend([1, 1, 5, 7])
print(my_list)

print("count, index, pop")
print(my_list.count(1))
my_list.insert(0, 11)
print(my_list.index(12))
print(my_list.pop())
print(my_list.pop())

print("reverse, sort")
my_other = my_list
my_list.reverse()
my_list.sort()
print(my_list)
print(my_list.sort())  # returns none
my_other.sort(reverse=True)
print(my_other)

print("uniting two lists")
my_list2 = [5, 6, 7, 3, 8, 4, 9, 10]
print(my_list2)

print("original: {},\nsorted: {}".format(my_list2, sorted(my_list2)))
my_list3 = my_list + my_list2
print("united: {}".format(my_list3))

print("doubling")
my_list4 = [1, 2, 3]
my_list5 = my_list4 * 2
print(my_list5, len(my_list5))

print("list of lists")
my_list6 = [my_list4, my_list5]
print(my_list6)
