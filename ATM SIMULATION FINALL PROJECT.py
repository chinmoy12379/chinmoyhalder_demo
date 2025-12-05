balance = int(input ("enter your balance: "))
pin = int(input("set your pin"))

enter_pin = int(input("enter your pin:"))

if enter_pin == pin:
    print("access granted")
else:
    print("wrong pin")
    exit()

while True:
    print("\n===dashboard===")
    print("1. check balance")
    print("2. withdraw balance")
    print("3. deposite balance")
    print("4. settings")
    print("5. exit")

    choise = input("enter your choise:")

    if choise == "1":
        print("your balance is: ", balance, "tk")
    elif choise == "2":
        withdraw = int(input("enter your withraw amount:"))
        if withdraw <= balance:
            balance -= withdraw
            print("successfully withdraw!", "you withdraw is", withdraw, "tk")
            print("remaining your balance is:", balance, "tk")
        else:
            print("insufficient balance")
   
    elif choise == "3":
        deposite = int(input("enter you deposite amount: "))
        balance += deposite
        print("deposite successfully!", "your deposite is:",deposite,"tk")
        print("now your total balance is:", balance,"tk")

    elif choise == "4":
        print("\n===settings manu===")
        print("1. change pin")
        print("2. manu")

        setting_choise = int(input("enter your setting choise:"))

        if setting_choise == 1:
            setting_pin = int(input("enter current pin: "))
            if setting_pin == pin:
                new_pin = int(input("enter your new pin:"))
                pin = new_pin
                print("seccussfully pin changed!")
            else:
                print("wrong pin")
       
        elif setting_choise == 2:
            print("menu")
            continue
   
    elif choise == "5":
        print("thank you for using me/atm")
        break
    else:
        print("invalid choise! please try again")

        