def register_Pin():
    Set_pin = input("Create A 4DIGITS PIN FOR YOUR ATM: ")
    if len(Set_pin) == 4 and Set_pin.isdigit():
        print("pin created successfully\n")
        return Set_pin
    else:
        print("invalid pin, please enter exactly 4 digits!!!\n")
        return register_Pin()

set_pin = register_Pin()

def login_pin():
    Pin = input("Enter your pin: ")
    
    if Pin == set_pin:
        print("correct pin!!\n")
        return True
    else:
        print("Incorrect pin, access denied!!\n")
        return False
    

def Show_Menu():
    if not login_pin():
        return 
    
    Balance = 1000
    while True:
        print("=================MENU================ \n")
        print("1. Check Balance\n")
        print("2. Deposit\n")
        print("3. Withdraw\n")
        print("4. Exit\n")
        print("=====================================\n")
        
        Choice = input("Enter your choice:")
        

        if Choice == "1":
            print(f"your balance is ${Balance}")
        
        elif Choice == "2":
            Amount = float(input("How much do you want to deposit: "))
            Balance += Amount
            print(f"Deposit successful!!!, your new balance is ${Balance}\n")

        elif Choice == "3":
            withdraw = float(input("How much do you want to withdraw: "))

            if withdraw < Balance:
                Balance -= withdraw
                print(f"Withdrawal successful!!! and your remaining balance is ${Balance}\n")

            else:
                print("insufficient balance!!!\n")


        elif Choice == "4":
            print("THANK YOU FOR CHOOSING OUR ATM. GOODBYE!!!\n")
            break

        else:
            print("Access denied could not login.\n")

            

print("===========================================================================================")
print("SIMPLE ATM SYSTEM")
print("===========================================================================================")


Show_Menu()
    