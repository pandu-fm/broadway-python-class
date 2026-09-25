# # Question 1

# class BankAccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Rs. {amount} deposited successfully.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Rs. {amount} withdrawn successfully.")
#         else:
#             print("Insufficient balance.")

#     def display_balance(self):
#         print(f"Current Balance: Rs. {self.balance}")


# class SavingsAccount(BankAccount):
#     def __init__(
#         self,
#         account_number,
#         account_holder,
#         balance,
#         interest_rate
#     ):
#         super().__init__(account_number, account_holder, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print(f"Interest: Rs. {interest}")
#         return interest


# print("\n===== QUESTION 1: SAVINGS ACCOUNT =====")

# savings = SavingsAccount(
#     "SA1001",
#     "Ram",
#     50000,
#     5
# )

# print(f"Account Holder: {savings.account_holder}")

# savings.deposit(10000)
# savings.withdraw(2000)

# savings.calculate_interest()
# savings.display_balance()


# # Question 2

# class CurrentAccount(BankAccount):
#     def __init__(
#         self,
#         account_number,
#         account_holder,
#         balance,
#         overdraft_limit
#     ):
#         super().__init__(account_number, account_holder, balance)
#         self.overdraft_limit = overdraft_limit

#     def withdraw_with_overdraft(self, amount):
#         maximum_withdrawal = self.balance + self.overdraft_limit

#         if amount <= maximum_withdrawal:
#             self.balance -= amount
#             print(f"Rs. {amount} withdrawn successfully.")
#         else:
#             print("Withdrawal exceeds overdraft limit.")


# print("\n===== QUESTION 2: CURRENT ACCOUNT =====")

# current = CurrentAccount(
#     "CA1001",
#     "Ram",
#     20000,
#     10000
# )

# current.withdraw_with_overdraft(25000)

# print(f"Remaining Balance: Rs. {current.balance}")


# # Question 3

# class SalaryAccount(BankAccount):
#     def __init__(
#         self,
#         account_number,
#         account_holder,
#         balance,
#         company_name,
#         employee_id
#     ):
#         super().__init__(account_number, account_holder, balance)

#         self.company_name = company_name
#         self.employee_id = employee_id

#     def credit_salary(self, salary):
#         self.balance += salary
#         print(f"Salary of Rs. {salary} credited successfully.")


# print("\n===== QUESTION 3: SALARY ACCOUNT =====")

# salary_account = SalaryAccount(
#     "SAL1001",
#     "Ram",
#     10000,
#     "ABC Pvt. Ltd.",
#     "EMP101"
# )

# print(f"Employee: {salary_account.account_holder}")
# print(f"Company: {salary_account.company_name}")
# print(f"Employee ID: {salary_account.employee_id}")

# salary_account.credit_salary(50000)

# salary_account.display_balance()


# # Question 4

# class FixedDepositAccount(BankAccount):
#     def __init__(
#         self,
#         account_number,
#         account_holder,
#         balance,
#         deposit_amount,
#         interest_rate,
#         duration_years
#     ):
#         super().__init__(account_number, account_holder, balance)

#         self.deposit_amount = deposit_amount
#         self.interest_rate = interest_rate
#         self.duration_years = duration_years

#     def calculate_maturity_amount(self):
#         interest = (
#             self.deposit_amount
#             * self.interest_rate
#             * self.duration_years
#             / 100
#         )

#         maturity_amount = self.deposit_amount + interest

#         print(f"Deposit Amount: Rs. {self.deposit_amount}")
#         print(f"Interest: Rs. {interest}")
#         print(f"Maturity Amount: Rs. {maturity_amount}")

#         return maturity_amount


# print("\n===== QUESTION 4: FIXED DEPOSIT =====")

# fixed_deposit = FixedDepositAccount(
#     "FD1001",
#     "Ram",
#     0,
#     100000,
#     8,
#     2
# )

# fixed_deposit.calculate_maturity_amount()


# # Question 5

# class StudentAccount(BankAccount):
#     def __init__(
#         self,
#         account_number,
#         account_holder,
#         balance,
#         student_id,
#         college_name,
#         student_discount
#     ):
#         super().__init__(account_number, account_holder, balance)

#         self.student_id = student_id
#         self.college_name = college_name
#         self.student_discount = student_discount

#     def display_student_account(self):
#         print("===== STUDENT ACCOUNT =====")
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: Rs. {self.balance}")
#         print(f"Student ID: {self.student_id}")
#         print(f"College: {self.college_name}")
#         print(f"Student Discount: {self.student_discount}%")


# print("\n===== QUESTION 5: STUDENT ACCOUNT =====")

# student_account = StudentAccount(
#     "ST1001",
#     "Sita",
#     25000,
#     "STU101",
#     "ABC College",
#     10
# )

# student_account.display_student_account()

# student_account.deposit(5000)
# student_account.withdraw(2000)

# student_account.display_student_account()



class BankAccount():
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self,amount):
        self.balance -= amount

    def deisplay_balance(self):
        print(self.balance)
 
 
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate, time):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
        self.time = time
 
    def display_balance(self):
        return (f"{self.account_holder} has {self.balance}")
   
    def calculate_interest(self):
        return(self.deposit*self.time*self.Interest_rate/100)
         
savings = SavingsAccount("001","P",2000,20,10)
savings.deposit(1000)
savings.deposit(4000)
savings.deisplay_balance()
savings.withdraw(20)
savings.deisplay_balance()