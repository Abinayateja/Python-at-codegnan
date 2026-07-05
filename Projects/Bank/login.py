from data import users

def login(account_number,password):
    if account_number in users and users[account_number]['password'] == password:
        return True
    else:
        return False