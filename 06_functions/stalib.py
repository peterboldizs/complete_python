import random
import shelve
import webbrowser

print(dir())
for di in dir():
    print(di)

print("*" * 40)
print("__builtins__")
for bi in dir(__builtins__):
    print(bi)

print("*" * 40)
print("shelve")
for si in dir(shelve):
    print(si)

print("*" * 40)
print("shelve.Shelf class")
for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

print("*" * 40)
help(shelve.Shelf)

print("*" * 40)
help(random.randint)

webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
help(webbrowser)

# windef = webbrowser.get(using='windows-default')
# windef.open("http://dzone.com")
