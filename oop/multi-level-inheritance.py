class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Balance: Rs. {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        interest_rate
    ):
        super().__init__(
            account_number,
            account_holder,
            balance
        )
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest: Rs. {interest}")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        interest_rate,
        bonus_rate
    ):
        super().__init__(
            account_number,
            account_holder,
            balance,
            interest_rate
        )
        self.bonus_rate = bonus_rate

    def calculate_bonus(self):
        bonus = self.balance * self.bonus_rate / 100
        print(f"Bonus: Rs. {bonus}")


account = PremiumSavingsAccount(
    "PS1001",
    "Ram",
    100000,
    5,
    2
)

account.deposit(10000)
account.withdraw(5000)

account.display_balance()
account.calculate_interest()
account.calculate_bonus()



class A:
    pass

class B:
    def print_data(self):
        pass

class C(A, B):
    pass

c = C()
c.print_data()