print("binary")
for i in range(17):
    print("{0:>2} in binary: {0:>08b}".format(i))
    
print("hex")
for i in range(17):
    print("{0:>2} in hex: {0:>02x}".format(i))

print("oct")
for i in range(17):
    print("{0:>2} in oct: {0:>03o}".format(i))

print(0b1110)
print(0xaa)

print("binary converter")
powers = []
for i in range(15, -1, -1):
    powers.append(2 ** i)

# print(powers)

x = int(input("Enter a number (max:65535):"))
print("{} in binary:".format(x))

printing = False
for power in powers:
    bit = x // power
    # eliminate leading zeros
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
        