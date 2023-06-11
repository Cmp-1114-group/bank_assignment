class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


def main():
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter your initial balance: "))
    bank_account = BankAccount(account_number, initial_balance)

    amount = float(input("Enter the amount to withdraw: "))
    if bank_account.withdraw(amount):
        print("Withdrawal successful.")
    else:
        print("Insufficient balance. Withdrawal failed.")


if __name__ == "__main__":
    main()
