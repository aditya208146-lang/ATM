from deposit import deposit
from withdraw import withdraw
from balance import show_balance
from statement import show_statement

while True:
    print("\nATM MENU")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        show_balance()
    elif ch == "2":
        deposit()
    elif ch == "3":
        withdraw()
    elif ch == "4":
        show_statement()
    elif ch == "5":
        break