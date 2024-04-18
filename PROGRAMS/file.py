#file cocepts     
fileptr = open("balaji.txt","a")     //append method
content = fileptr.write("\nnithin lists")
print(content)
fileptr.close()

fileptr = open("balaji.txt","r")  //read method
content = fileptr.read()
print(content)
fileptr.close()

fileptr = open("balaji.txt","w")
content = fileptr.write("\nnithin lists")
print(content)
fileptr.close()


