from data import users

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