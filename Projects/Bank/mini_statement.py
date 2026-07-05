from data import users

def mini_statement(account_number):
    if account_number in users:
        user = users[account_number]
        return f"Account Number: {account_number}\nName: {user['name']}\nEmail: {user['email']}\nBalance: {user['balance']}"
    else:
        return "User not found"