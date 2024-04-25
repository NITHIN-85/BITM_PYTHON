test_string=input("enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))


'''text = input("enter the string:")
c = input("enter the character:")
print(text.count(c))'''