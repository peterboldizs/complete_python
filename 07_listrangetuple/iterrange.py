print("iterator")
my_string = "0123456789"
for ch in iter(my_string):
    print(ch)
print("index of 4 is {}".format(my_string[4]))
print(my_string.index("4"))

my_list = ["A", "B", "C", "D", "E"]
my_iter = iter(my_list)
for i in range(0, len(my_list)):
    nextitem = next(my_iter)
    print(nextitem)

evenlist = list(range(0, 10, 2))
print(evenlist)
oddlist = list(range(1, 10, 2))
print(oddlist)

print("ranges")
r = range(20)
print(r)

for i in r[::-2]:
    print("counting {}".format(i))

for j in range(0, 20, -2):
    print(j)  # nothing
