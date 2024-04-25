#1
''''sample_data = input("Enter the binaryy number: " ).split(',')
print(sample_data)

for i in sample_data:
    if (int(i, 2)%5 == 0):
        print(int(i,2))
'''

#2
'''
sample_data=input("Enter the comb of string and dig: ")
print(sample_data)
leter_sum=0
dig_sum=0
for i in sample_data:
    if i.isalpha():
        leter_sum+=1

    elif i.isdigit():
        dig_sum+=1
print("Total number of letter's: ",leter_sum)
print("Total number of digit's: ",dig_sum)'''


#3 password valid or invalid

# at least 1 letter between a-z 
# 1 letter between A-Z
# at least 1 number between 0-9
# at least 1 character from $#@
# min length 6 charace
# max length 16 character

'''def passowrd_validator():
    password = input("enter your password : ")
    validator = {"a-z" : False, "A-Z" : False, "num" : False, "special_char": False, "min" : False, "max" : False}
    if (len(password) < 6 or len(password) > 16):
        print("invalid password")
        return
    else:
        validator["min"] = True
        validator["max"] = True
    
    for i in password:
        if (str.islower(i)):
            validator["a-z"] = True
        if (str.isupper(i)):
            validator["A-Z"] = True
        if (str.isdigit(i)):
            validator["num"] = True
        if (i == "$" or i == "#" or i == "@"):
            validator["special_char"] = True
    for key, value in validator.items():
        if (not value):
            print("invalid passoword")
            return 
    
    print("valid password")
       
       
passowrd_validator()'''

#4 print the format pattern in E
size = int(input("enter the size:"))
print_char = input("enter the char:")
print(print_char * (size // 2))
for i in range(2, size):
    if (size % 2 == 0 and (i == (size // 2) + 1 or i == (size // 2))):
        print(print_char * ((size // 2)))
    elif (i == (size // 2)+1):
        print(print_char * ((size // 2)))
    else:
        print(print_char)
print(print_char * (size // 2))