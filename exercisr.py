list_of_expences = []

def add_expense():
    name = input("Enter the name of the expense: ")
    expense_type = input("Enter the type of the expense: ")
    try:
        amount = int(input("Enter the amount of the expense: "))    
    except ValueError as e:
        print(f"Invalid input for amount. Please enter a valid integer. Error: {e}")
    expense = {"name": name, "amount": amount}
    list_of_expences.append(expense)


count = 0
while count < 3:
    add_expense()
    count += 1
