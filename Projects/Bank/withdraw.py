from data import users

def withdraw(account_number,withdraw_amount):
    if account_number in users:
        if users[account_number]['balance'] >= withdraw_amount:
            users[account_number]['balance'] -= withdraw_amount
            return f"Withdraw Successful. Remaining Balance: {users[account_number]['balance']}"
        else:
            return "Insufficient Balance"