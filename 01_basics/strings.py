print("Strings")
print("-" * 80)
print("Single/double/triple quotes")

print("Hello")
print('Hello world')
print("Hello it's time")

single = 'single quotes'
double = "double quotes"
triple = '''triple single quotes'''
triple_double = """triple
double
quotes"""
tabbed = '1\t2\t3\t4'

print(single)
print(double)
print(triple)
print(triple_double)
print(len(triple_double))
print(tabbed)

print("-" * 80)
print("Concat/split")
greet = "Hello"
nname = 'Peter'
print(greet + " " + nname)

split1 = """split
over
several
lines"""
split2 = """split
\tover
\t\tseveral
\t\t\tlines"""
pet = '''the owner said "He \'s resting"'''
pet2 = """the owner said "He \'s resting" """
bigstring = "This is \n a big string \n in more llines"

print(split1)
print(split2)
print(pet)
print(pet2)
print(bigstring)

print("-" * 80)
print("Encoding/decoding/slicing")
str5 = "árvíztűrő tükörfúrógép"
print(type(str5))
print(str5)
e_str5 = str5.encode('utf-8')
print(type(e_str5))
print(e_str5)
de_str5 = e_str5.decode('utf-8')
print(type(de_str5))
print(de_str5)
str6 = "This is the beginning of a beautiful friendship"
print(str6[2:34:3])
print(str6[::-1])

str11 = "this is \nnew line\t\ttabbed"
raw_string = r"this is \nnew line\t\ttabbed"
b_string = "this is" + chr(10) + "new line " + chr(9) + chr(9) + "tabbed"
print(str11)
print(raw_string)
print(b_string)

print("-" * 80)
print('String formatting, positional')
age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} "
      .format(31, "January", "March", "May", "July", "August", "October", "December"))

print("January: {2}, February: {0}, March: {2}, April: {1}, May: {2}, June: {1}, "
      "July: {2}, August: {2}, September: {1}, October: {2}, November: {1}, December: {2}".format(28, 30, 31))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))


for i in range(1, 5):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("Pi is approximately %12f" % (22 / 7))

for i in range(1, 5):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 5):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    
for i in range(1, 5):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

