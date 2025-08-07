# f = open("sample.txt", "rt")
# print(f.read())
# print(f.readline())
# f.close()

# Don't have to worry about file closing
with open("sample.txt") as f:
    # print(f.read())
    print(f.read(3))
    print(f.readline())
    print(f.readline())

with open("sample2.txt", "w") as f1:
    f1.write("This is a new sample file \n")

with open("sample2.txt", "a") as f2:
    f2.write("This is a new line")

with open("sample2.txt") as f3:
    print(f3.read())


import os
os.remove("sample.txt")