User = "nico"
Password = 12345
Money = 1000

def Inputs ():

    User_in = str(input("Username: "))

    Password_in = int(input("Password: "))

    if User_in == User:

        if Password_in == Password:

            print("Successful Login")

            Transactions()

        else:

            print("Incorrect Password")

    else:

        print("Incorrect Username")

def Transactions():

    print("¿What do you want to do?")

    Option = int(input("1. Deposit Money o 2. Withdrawals "))

    if Option == 1:

        Deposit = int(input("¿How much money de you want to deposit? "))

        Deposited = Money + Deposit

        print(Deposited)

        print("Successful deposit")

    elif Option == 2:

        Withdrawal = int(input("¿How much money do you want to withdrawals? "))

        if Withdrawal < Money:

            withdrawn = Money - Withdrawal

            print(withdrawn)

            print("Successful withdrawals")

        else:

            print("You do not have enough money")

    else:

        print("Error")

Inputs()