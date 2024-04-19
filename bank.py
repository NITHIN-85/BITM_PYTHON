balance = 0
def deposit():
    amount = int(input("enter deposit amount: "))
    bank_account["balance"] += amount


def withdraw():
    amount = int(input("enter withdrawl amount: "))
    if amount > bank_account["balance"]:
        print("insufficent funds")
    else:
        print("amount withdrawn : ", str(amount))
        bank_account["balance"] -= amount

def get_balance():
    print(bank_account["balance"])

bank_account = {"balance" : balance, "depsoit" : deposit, "withdraw" : withdraw, "get_balance" : get_balance}
bank_account["balance"] = 0
def print_choces():
    print("1. display balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

database = {"abc@gmail.com" : 123456 }

def login():
    uemail = input("enter your email : ")
    passowrd = int(input("enter your password : "))
    if uemail not in database:
        print("invalid email, exit")
        return
    
    if passowrd != database[uemail]:
        print("invalid password, exit")
        return 
    
    print("login succesfull")
    while True:
        print_choces()
        choice = int(input("enter your choice : "))
        if choice == 1:
            bank_account["get_balance"]()
        elif choice == 2:
            bank_account["depsoit"]()
        elif choice == 3:
            bank_account["withdraw"]()
        elif choice == 4:
            return
        else:
            print("invalid choice try again!")

login()
