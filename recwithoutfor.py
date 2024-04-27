def print_nums(num,i):
    if i >num:
        return
    else:
        print(i, end=" ")
        print_nums(num,i+1)
print_nums(100,1)