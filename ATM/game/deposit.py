import account

def deposit():
    amt = float(input("Enter amount: "))
    account.amount = account.amount + amt
    account.transactions.append(f"Deposited {amt}")
    print("Deposited successfully")