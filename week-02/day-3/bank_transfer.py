


accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def name_balance(acc_number):
    for i in range(len(accounts)):
        if accounts[i]['account_number'] == acc_number:
            return [accounts[i]['client_name'], accounts[i]['balance']]

def transfer_cash(from_acc, to_acc, amount):

    from_acc_ok = False
    to_acc_ok = False

    for i in range(len(accounts)):
        if accounts[i]['account_number'] == from_acc:
            from_acc_ok = True
            if accounts[i]['balance'] - amount < 0:
                return '505 - money not found'
        if accounts[i]['account_number'] == to_acc:
            to_acc_ok = True
    
    if not(from_acc_ok and to_acc_ok):
        return '404 - account not found'

    for i in range(len(accounts)):
        if accounts[i]['account_number'] == from_acc:
            accounts[i]['balance'] -= amount
        if accounts[i]['account_number'] == to_acc:
            accounts[i]['balance'] += amount

    return 'transfer done'

print(name_balance(11234543))
print(name_balance(23456311))

print(transfer_cash(23456311, 11234543, 938475))

print(name_balance(11234543))
print(name_balance(23456311))