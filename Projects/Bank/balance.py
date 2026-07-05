from data import users

def balance(account_number):
    if account_number in users:
        return users[account_number]['balance']
    else:
        return "User not found"