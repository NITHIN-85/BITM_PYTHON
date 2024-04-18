name = "NITHIN"
print(name)
for i in range(1, len(name)-1):
    print(" " * (len(name) - i -1),end="")
    print(name[-i - 1])
print(name)