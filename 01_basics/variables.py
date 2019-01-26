print("variables")
greeting = "Good day"
strvar = "qa"
_strvar = "ws"
intvar = 24
_intvar = 2
# 1var = "we not good"
print(strvar + ' ' + _strvar)
#print(strvar + ' ' + intvar) TypeError: Can't convert 'int' object to str implicitly
print(intvar * _intvar)

# now with input
inp = input("please enter your name: ")
print(greeting + ' ' + inp)
