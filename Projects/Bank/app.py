# User Table
users = {
    1234: {'name': "Abi", 'email': "gaddamabinayateja@gmail.com",'balance': 5000, 'password' : "1234"},
    1235: {'name': "Teja", 'email': "abinayatejagaddam@gmail.com",'balance': 10000, 'password' : "1235"}
    }

def register(name,email,initial_deposite,password):
    pass

def login(account_number,password):
    if account_number in users and users[account_number]['password'] == password:
        return True
    else:
        return False

# Balance function definition
def balance(account_number):
    if account_number in users:
        return users[account_number]['balance']
    else:
        return "User not found"

# Withdraw function definition
def withdraw(account_number,withdraw_amount):
    if account_number in users:
        if users[account_number]['balance'] >= withdraw_amount:
            users[account_number]['balance'] -= withdraw_amount
            return f"Withdraw Successful. Remaining Balance: {users[account_number]['balance']}"
        else:
            return "Insufficient Balance"

# Deposite function definition
def deposite(account_number,deposite_amount):
    if account_number in users:
        users[account_number]['balance'] += deposite_amount
        return f"Deposite Successful. Current Balance: {users[account_number]['balance']}"

# Transfer function definition
def transfer(sender_account_number,receiver_account_number,transfer_amount):
    if sender_account_number in users and receiver_account_number in users:
        if users[sender_account_number]['balance'] >= transfer_amount:
            users[sender_account_number]['balance'] -= transfer_amount
            users[receiver_account_number]['balance'] += transfer_amount
            return f"Transfer Successful. Remaining Balance: {users[sender_account_number]['balance']}"
        else:
            return "Insufficient Balance"
    else:
        return "User not found"

#  Mini statement function definition
def mini_statement(account_number):
    if account_number in users:
        user = users[account_number]
        return f"Account Number: {account_number}\nName: {user['name']}\nEmail: {user['email']}\nBalance: {user['balance']}"
    else:
        return "User not found"

# Logout function definition
def logout():
    login_val = False
    return "Logout Successful"



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
    

