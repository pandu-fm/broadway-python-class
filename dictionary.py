""""dictionary.py: This module contains the implementation 
of a dictionary data structure."""

name = "name"

user_info = {
    name: "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": "123 Main St, Anytown, USA",
    "phone": "555-1234",
    "users": ["user1", "user2", "user3"], # to store multiple values in a single key
}

# print(user_info.keys())
# print(user_info.values())
# print(user_info.items())


# to get the single information from the dictionary
print(user_info["name"])
print(user_info["age"])
print(user_info["email"])
print(user_info["address"])

# update single value in the dictionary
user_info["age"] = 32
user_info["has_vehicle"] = True

print(user_info)

# to update multiple values in the dictionary
user_info.update({"model": "test", "gender": "M"})

user_info["users"].append("user4")  # to add a new value in the list of users

# to delete the data from dictionary
del user_info["phone"]  # to delete a single key-value pair

print(user_info)




