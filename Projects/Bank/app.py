# User Table
users = {
    1234: {'name': "Abi", 'email': "gaddamabinayateja@gmail.com",'balance': 5000, 'password' : "1234"},
    1235: {'name': "Teja", 'email': "abinayatejagaddam@gmail.com",'balance': 10000, 'password' : "1235"}
    }

def register(name,email,initial_deposite,password):
    pass

def login(account_number,password):
    pass

# Balance function definition
def balance(account_number):
    pass

# Withdraw function definition
def withdraw(account_number,withdraw_amount):
    pass

# Deposite function definition
def deposite(account_number,deposite_amount):
    pass

# Transfer function definition
def transfer(sender_account_number,receiver_account_number,transfer_amount):
    pass

#  Mini statement function definition
def mini_statement(account_number):
    pass

# Logout function definition
def logout():
    pass



# main
if __name__ == "__main__":

    print("Welcome to small scale bank")
    print("1. Register \n 2. Login")
    choice = int(input("Select Your Choice: "))

    # calling register function
    if choice == 1:
        print("Under Development Process")
    elif choice == 2:
        account_number = int(input("Enter Your Account Number: "))
        password = input("Enter Your Password: ")
        login_val = login(account_number=account_number,password=password)

        while login_val:
            print("The Small Scale Bank Providing Servies")
            print("1. Balance /n 2. Withdraw /n 3. Deposite \n 4. Transfer \n 5. Mini-Statement \n 6. Logout")
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
                res = deposite(account_number=account_number, deposite_amount=deposite)
                print(res)
                
            elif choice == 4:
                receiver_account_number = int(input("Enter Receiver Account Number: "))
                amount = int(input("Enter Your Transfer Ammount: "))
                # call transfer function
                res = transfer(sender_account_number=account_number,receiver_account_number=receiver_account_number,transfer_amount=amount)
                print(res)
            elif choice == 5:
                
    

