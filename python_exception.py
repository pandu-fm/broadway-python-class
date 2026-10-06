"""
This module defines a custom exception class for handling errors in Python code. 
The `PythonException` class inherits from the built-in `Exception` class and can 
be used to raise specific exceptions related to Python code execution.
"""

print("Loading python_exception.py module...")

try:
    print(5/0)
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")


data = {
    "name": "John Doe",
}


try:
    print(f"Data: {data["name"]}")
except KeyError as error:
    print(f"Error occurred: {error}")


try:
    print(5/0)
except Exception as e:
    print(f"Error occurred: {e}")



# try:
#     Khalti().pay()
# except Exception as e:
#     print("Failed to process payment:", e)


# Khalti().pay()


try:
    open("non_existent_file.txt", "r")
except FileNotFoundError as e:
    # create_log_file("non_existent_file.txt", str(e))
    pass

# syntax error
# def help()
#    pass


# logical error
age = 2
if age == 4:
    print("Admit to class 12")


def parse_age():
    age = input("Enter your age: ")
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        return age
    except ValueError as e:
        print(f"please provide a valid age with integer: {e}")
        return None

parse_age()

try:        
    result = [1,3,4] + {"name": "John"}  # This will raise a TypeError 
except TypeError as e:
    print(f"Error occurred -------------: {e}")


def validtae_email(email):
    if "@" not in email:
        raise ValueError("Invalid email address.")
    return True

try:
    data = validate_email("example.com")  # This will raise a ValueError       
except ValueError as e:
    print(f"Error occurred: {e}")

print("python_exception.py module loaded successfully.")

