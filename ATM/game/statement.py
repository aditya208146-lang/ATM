from account import transactions

def show_statement():
    print("Transactions:")
    for t in transactions:
        print(t)