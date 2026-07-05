# User Table
from data import users
from login import login
from balance import balance
from withdraw import withdraw
from deposite import deposite
from transfer import transfer
from mini_statement import mini_statement
from logout import logout

users = users

# main
if __name__ == "__main__":

    print("Welcome to small scale bank")
    print("1. Register \n2. Login")
    choice = int(input("Select Your Choice: "))

    # calling register function
    if choice == 1:
        print("Under Development Process")
    elif choice == 2:
        account_number = int(input("Enter Your Account Number: "))
        password = input("Enter Your Password: ")
        login_val = login(account_number=account_number,password=password)
        if not login_val:
            print("Invalid Account Number or Password")
        while login_val:
            print("-------------------------------------------------------------------------")
            print("The Small Scale Bank Providing Servies")
            print("1. Balance \n2. Withdraw \n3. Deposite \n4. Transfer \n5. Mini-Statement \n6. Logout")
            print("-------------------------------------------------------------------------")
            choice = int(input("Enter Your Choice: "))
            
            if choice == 1:
                # call Balance function
                current_balance = balance(account_number= account_number)
                print(f"Current Balance is: {current_balance}")
            elif choice == 2:
                amount = int(input("Enter Your WithDraw Ammount: "))
                # call withdraw funtion
                res = withdraw(account_number=account_number,withdraw_amount=amount)
                print(res)

            elif choice == 3:
                amount = int(input("Enter Your Deposite Ammount: "))
                # call deposite function
                res = deposite(account_number=account_number, deposite_amount=amount)
                print(res)
                
            elif choice == 4:
                print(f"Sender Balance: {users[account_number]['balance']}")
                receiver_account_number = int(input("Enter Receiver Account Number: "))
                amount = int(input("Enter Your Transfer Ammount: "))
                # call transfer function
                res = transfer(sender_account_number=account_number,receiver_account_number=receiver_account_number,transfer_amount=amount)
                print(res)
            elif choice == 5:
                # call mini statement function
                res = mini_statement(account_number=account_number)
                print(res)
            elif choice == 6:
                # call logout function
                res = logout()
                print(res)
                break
            else:
                print("Invalid Choice: Please Select from  1-6")
    

