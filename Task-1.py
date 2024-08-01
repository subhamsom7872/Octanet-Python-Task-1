# atm_machine.py
import time

print("Welcome to Rajput Bank")

time.sleep(2)

print("Please insert your card")

time.sleep(2)
class ATM:

    def __init__(self):
        self.balance = 50000

    def deposit(self, amount):
        """Deposit money into account"""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw money from account"""
        if self.balance < amount:
            print("Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        """Check account balance"""
        print(f"Current balance: ${self.balance}")

def main():
    atm = ATM()

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()