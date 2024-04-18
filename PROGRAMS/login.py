email="nithin@gmail.com"
pwd=654321
otp=7890
uemail=str(input("Enter the email"))
uepwd=int(input("Enter the password"))
ueotp=int(input("enter the otp"))
if(email == uemail):
    if(pwd == upwd):
        if(otp == ueotp):
            
            print("login sucess")
else:
    print("login failed due to incorrect pwd")
else:
    print("login failed due to incorrect email")
else:
    print("login failed due to incorrect otp")
else:
    print("login sucess  correct otp")
