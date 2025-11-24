from datetime import datetime

class BankAccount:
    def __init__(self, acc_no, name, pin, acc_type="Savings", balance=0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.acc_type = acc_type
        self.balance = balance
        self.transactions = []

    def add_transaction(self, type, amount):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{time} - {type}: ₹{amount} | Balance: ₹{self.balance}")


    def display(self):
        print(f"Account: {self.acc_no} | {self.name} | {self.acc_type} | Balance: ₹{self.balance}")


class BankingSystem:
    def __init__(self):
        self.accounts = []
        self.logged_in = None

    def create_account(self):
        print("\n--- Create New Account ---")
        acc_no = int(input("Enter Account Number: "))
        for a in self.accounts:
            if a.acc_no == acc_no:
                print("Account number already exists!\n")
                return
        name = input("Enter Name: ")
        pin = input("Set 4-digit PIN: ")
        acc_type = input("Enter Account Type (Savings/Current): ").capitalize()
        balance = float(input("Initial Deposit: ₹"))
        acc = BankAccount(acc_no, name, pin, acc_type, balance)
        acc.add_transaction("Account Created", balance)
        self.accounts.append(acc)
        print(f"Account created successfully for {name}!\n")

    def login(self):
        print("\n--- Login ---")
        acc_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")
        for a in self.accounts:
            if a.acc_no == acc_no and a.pin == pin:
                self.logged_in = a
                print(f" Welcome {a.name}!\n")
                return
        print("Invalid Account or PIN!\n")

    def logout(self):
        if self.logged_in:
            print(f"Logged out from {self.logged_in.name}'s account.\n")
            self.logged_in = None
        else:
            print("No user logged in.\n")

    def deposit(self):
        if not self.logged_in:
            print("Login first!\n")
            return
        amount = float(input("Enter amount to deposit: ₹"))
        self.logged_in.balance += amount
        self.logged_in.add_transaction("Deposit", amount)
        print(f"Deposited ₹{amount} successfully!\n")

    def withdraw(self):
        if not self.logged_in:
            print("Login first!\n")
            return
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount > self.logged_in.balance:
            print("Insufficient balance!\n")
        else:
            self.logged_in.balance -= amount
            self.logged_in.add_transaction("Withdraw", amount)
            print(f"Withdrawn ₹{amount} successfully!\n")

    def transfer(self):
        if not self.logged_in:
            print("Login first!\n")
            return
        target_acc = int(input("Enter Receiver Account Number: "))
        amount = float(input("Enter amount to transfer: ₹"))
        receiver = None
        for a in self.accounts:
            if a.acc_no == target_acc:
                receiver = a
        if not receiver:
            print("Receiver account not found!\n")
            return
        if amount > self.logged_in.balance:
            print("Not enough balance!\n")
            return
        self.logged_in.balance -= amount
        receiver.balance += amount
        self.logged_in.add_transaction(f"Transfer to {receiver.name}", amount)
        receiver.add_transaction(f"Received from {self.logged_in.name}", amount)
        print(f"₹{amount} transferred to {receiver.name}!\n")

    def check_balance(self):
        if not self.logged_in:
            print("Login first!\n")
            return
        print(f"Current Balance: ₹{self.logged_in.balance}\n")

    def transaction_history(self):
        if not self.logged_in:
            print("Login first!\n")
            return
        print(f"\nTransaction History for {self.logged_in.name}")
        print("-----------------------------------------")
        for t in self.logged_in.transactions:
            print(t)
        print()

    def change_pin(self):
        if not self.logged_in:
            print("Login first!\n")
            return
        old_pin = input("Enter Old PIN: ")
        if old_pin != self.logged_in.pin:
            print("Incorrect PIN!\n")
            return
        new_pin = input("Enter New 4-digit PIN: ")
        self.logged_in.pin = new_pin
        print("PIN updated successfully!\n")


    # Admin features
    def admin_dashboard(self):
        admin_pass = input("Enter Admin Password: ")
        if admin_pass != "admin123":
            print("Wrong admin password!\n")
            return
        print("\n====== Admin Dashboard ======")
        total = sum(a.balance for a in self.accounts)
        print(f"Total Accounts: {len(self.accounts)}")
        print(f"Total Bank Money: ₹{total}")
        print("\n-- All Accounts --")
        for a in self.accounts:
            a.display()
        print("================================\n")

    def delete_account(self):
        admin_pass = input("Enter Admin Password: ")
        if admin_pass != "admin123":
            print("Wrong admin password!\n")
            return
        acc_no = int(input("Enter Account Number to delete: "))
        for a in self.accounts:
            if a.acc_no == acc_no:
                self.accounts.remove(a)
                print(f"Account {a.name} deleted!\n")
                return
        print("Account not found!\n")


def main():
    bank = BankingSystem()

    while True:
        print("========== BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. Check Balance")
        print("7. Transaction History")
        print("8. Change PIN")
        print("9. Admin Dashboard")
        print("10. Delete Account (Admin)")
        print("11. Logout")
        print("12. Exit")

        choice = input("Enter your choice (1-13): ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.login()
        elif choice == '3':
            bank.deposit()
        elif choice == '4':
            bank.withdraw()
        elif choice == '5':
            bank.transfer()
        elif choice == '6':
            bank.check_balance()
        elif choice == '7':
            bank.transaction_history()
        elif choice == '8':
            bank.change_pin()
        elif choice == '9':
            bank.admin_dashboard()
        elif choice == '10':
            bank.delete_account()
        elif choice == '11':
            bank.logout()
        elif choice == '12':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
