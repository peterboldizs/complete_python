sb = open("sbdemo.txt", "r")
for line in sb:
    if "API" in line:
        print(line)
sb.close()

print("-" * 40)
print("using with")
with open("sbdemo.txt", "r") as sb2:
    for line in sb2:
        print(line)

print("-" * 40)
print("readline")
with open("sbdemo.txt", 'r') as sb3:
    line = sb3.readline()
    while line:
        print(line, end='')
        line = sb3.readline()

print("-" * 40)
print("readlines")
with open("sbdemo.txt", 'r') as sb4:
    lines = sb4.readlines()
print(lines)

print("lines processed as list")
for l in lines:
    print(l, end='')

print("-" * 40)
print("lines processed backwards")
for l in lines[::-1]:
    print(l, end='')

print("-" * 40)
print("text processed backwards")
with open("sbdemo.txt", 'r') as sb5:
    lines = sb5.read()
for l in lines[::-1]:
    print(l, end='')
