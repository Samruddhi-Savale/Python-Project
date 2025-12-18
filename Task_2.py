# Task 2:
# ATM Simulator
""" Create a program that simulates all the ATM functionalities and operations (CheckBalance,
    Deposite, Withdraw)"""

import time as t
pin = int(input("Enter the Pin code: "))
balance = float(input("Enter the balance: "))
name = input("Enter the User name: ").strip().title()
print("****************************************")
print(f"\n\n Welcome To Your Bank Accout ",name, end = "\n")
choice = 5
while(True):
    print("\t\t0. Logout And Exit")
    print("\t\t1. View Accout Balance")
    print("\t\t2. Deposite Cash")
    print("\t\t3. Withdraw Cash")
    print("\t\t4. Change PIN")
    print("\n")
    choice = int(input("Enter number to proceed > "))
    print("\n\n")
    if choice == 0:
        print("Exiting.....")
        t.sleep(2)
        print("You have been Logged Out. \n Thank You! \n\n")
        break
    elif choice in(1,2,3,4):
        num_of_tries = 3
        while(num_of_tries != 0):
            input_pin = int(input("Please Enter Your 4 Digit PIN > "))
            if input_pin == pin:
                print("Accout Authorized! \n\n")
                if choice == 1:
                    print("Loading Account Balance....")
                    t.sleep(1.5)
                    print("Your Current Balance is Rs. ", balance, end = "\n\n\n")
                    break
                elif choice == 2:
                    print("Loading Cash Deposite....")
                    t.sleep(1.5)
                    deposite = int(input("Enter the amount you wish to deposite > ")) 
                    print("Depositing Rs. ",deposite)
                    confirm = input("Confirm?  Y/N > ")
                    if confirm in('Y', 'y'):
                        balance += deposite
                        print("Amount Deposited - Rs. ",deposite)
                        print("Upadated Balance - Rs. ",balance, end = "\n\n\n")
                    else:
                        print("Cancelling Transaction....")
                        t.sleep(1)
                        print("Transaction Cancelled! \n\n")
                    break
                elif choice == 3:
                    print("Opening Cash Withdrawal....")
                    t.sleep(1.5)
                    while(True):
                        withdraw = float(input("Enter the amount you wish to withdraw > "))
                        if withdraw > balance:
                            print("Can't withdraw Rs. ",withdraw)
                            print("Please, Enter the lower amount!")
                            continue
                        else:
                            print("Withdrawing Rs. ",withdraw)
                            confirm = input("Confirm?  Y/N > ")
                            if confirm in('Y', 'y'):
                                balance -= withdraw
                                print("Amount Withdrawn - Rs. ",withdraw)
                                print("Remaining Balance - Rs. ",balance, end = "\n\n\n")
                            else:
                                print("Cancelling Transaction....")
                                t.sleep(1)
                                print("Transaction Cancelled!")
                                break
                    break    
                elif choice == 4:
                    print("Loading PIN Change....")
                    t.sleep(1.5)
                    pin_new = int(input("Enter Your New PIN > "))
                    print("Changing PIN to ",pin_new)
                    confirm = input("Confirm?  Y/N > ")
                    if confirm in('Y', 'y'):
                        pin = pin_new
                        print("PIN Changed Successfully! \n\n")
                    else:
                        print("Cancelling PIN Change....")
                        t.sleep(1)
                        print("Process Cancelled! \n\n")
                    break
                else:
                    print("PIN Incorrect!")
                    print("Number of tries left - ",num_of_tries, end = "\n\n")
            else:
                print("Exiting....")
                t.sleep(2)
                print("You Have Been Logged Out. \n Thank You! \n\n")
                break
    else:
        print("Invalid Input!")
        print("\t\t0. Enter 0 to Logout and Exit")
        continue
        
