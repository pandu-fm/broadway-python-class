broadway_info = "Hello from.brodway.tinkune."
print(broadway_info.capitalize())
print(broadway_info.upper())
print(broadway_info.split(" "))
print(broadway_info.split("."))

password = " Hello@123                 "
print(len(password))
password = password.strip()
print(len(password))

email ="bRoadway@ExaMple.com"
print(email.lower())


# string format

name = "Charlie"
age = 35
information = "My name is {} and I am {} years old."
# print(information.format("Alice", 25))
# print(information.format("Bob", 30))
print(f"My name is {name} and I am {age} years old.")
name = "Alice"
print(f"My name is {name} and I am {age} years old.")

# join in stirng
fruits = ["apple", "banana", "cherry"]
print("!".join(fruits))