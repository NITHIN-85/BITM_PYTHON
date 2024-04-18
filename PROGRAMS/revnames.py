names="balaji srinivasan"
print(names)
print(names[-1::-3])

for i in range(0,len(names),2):
    print(names[i : i+2],end='-')
print()


for i in range (1,len(names)+1):
    if(i %3==0):
        print("-", end="")
    else:
        print(names[i-1], end="")
        
    
