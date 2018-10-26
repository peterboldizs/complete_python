print("Strings")

print("Hello")
print('Hello world')
print("Hello it's time")
greet = "Hello"
nname = 'Peter'
print(greet + " " + nname)
bigstring = "This is \n a big string \n in more llines"
tabbed = '1\t2\t3\t4'

spl = """split
over
several
lines"""
sp2 = """split
\tover
\t\tseveral
\t\t\tlines"""

pet = '''the owner said "He \'s resting"'''
pet2 = """the owner said "He \'s resting" """
print(bigstring)
print(tabbed)
print(spl)
print(sp2)
print(pet)
print(pet2)

str1 = 'single quotes'
str2 = "double quotes"
str3 = '''triple
single quotes'''
str4 = """triple
double
quotes"""
print(str1)
print(str2)
print(str3)
print(str4)
print(len(str4))
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

print('string formatting')
age = 24
print("my age is " + str(age))
print("my age is {0}".format(age))
print("my age is %d" % age)
print("""
Jan: {2}
Feb: {0}
Mar: {1}
""".format(28, 30, 31))

str11 = "this is \nnew line\t\ttabbed"
raw_string = r"this is \nnew line\t\ttabbed"
b_string = "this is" + chr(10) + "new line " + chr(9) + chr(9) + "tabbed"
print(str11)
print(raw_string)
print(b_string)
