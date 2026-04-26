import account

def withdraw():
    amt = float(input("Enter amount: "))
    if amt > account.amount:
        print("Insufficient balance")
    else:
        account.amount -= amt
        account.transactions.append(f"Withdrawn {amt}")
        print("Withdrawn successfully")