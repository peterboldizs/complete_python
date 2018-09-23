with open("binfile", 'bw') as bin_file:
    for i in range(6):
        bin_file.write(bytes([i]))

print("-" * 30)
print("binary read")
with open("binfile", 'br') as bin_file2:
    for b in bin_file2:
        print(b)

print("-" * 30)
print("variables to binary")
a = 65534
b = 65535
c = 65536
x = 2998302
with open("binfile2", 'bw') as bin_file3:
    bin_file3.write(a.to_bytes(2, 'big'))
    bin_file3.write(b.to_bytes(2, 'big'))
    bin_file3.write(c.to_bytes(4, 'big'))
    bin_file3.write(x.to_bytes(4, 'big'))
    bin_file3.write(x.to_bytes(4, 'little'))

print("-" * 30)
print("variables from binary")
with open("binfile2", 'br') as bin_file4:
    e = int.from_bytes(bin_file4.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file4.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file4.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file4.read(4), 'big')
    print(h)
    # i = int.from_bytes(bin_file4.read(4), 'little')
    # print(i)
    i = int.from_bytes(bin_file4.read(4), 'big')
    print(i)

# bin_file3.read()