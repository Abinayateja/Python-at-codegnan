from data import users

def deposite(account_number,deposite_amount):
    if account_number in users:
        users[account_number]['balance'] += deposite_amount
        return f"Deposite Successful. Current Balance: {users[account_number]['balance']}"