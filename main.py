from datetime import datetime


class Amount:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: {self.amount:.2f}"


class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            print("Сумма депозита должна быть положительной.")
            return
        transaction = Amount(amount, 'DEPOSIT')
        self.transactions.append(transaction)
        self.balance += amount
        print(f"Внесено {amount:.2f}. Текущий баланс: {self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
            return
        if amount > self.balance:
            print("Недостаточно средств на счете.")
            return
        transaction = Amount(amount, 'WITHDRAWAL')
        self.transactions.append(transaction)
        self.balance -= amount
        print(f"Снято {amount:.2f}. Текущий баланс: {self.balance:.2f}")

    def print_transaction_history(self):
        print(f"История транзакций для счета {self.account_number} ({self.account_holder}):")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"Счет #{self.account_number}, Владелец: {self.account_holder}, Баланс: {self.balance:.2f}"

    def __add__(self, amount: float):
        self.deposit(amount)
        return self

    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self


if __name__ == "__main__":
    account_number = int(input("Введите номер счета: "))
    account_holder = input("Введите имя владельца счета: ")
    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\n1. Внести деньги\n2. Снять деньги\n3. Проверить баланс\n4. История транзакций\n5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            amount = float(input("Введите сумму для внесения: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Текущий баланс: {account.get_balance():.2f}")
        elif choice == "4":
            account.print_transaction_history()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
