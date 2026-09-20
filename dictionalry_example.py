# # contact book
# contacts = {
#     "kshan":0000000000000,
#     "numananda":1111111111,
#     "prasil":2222222222,
#     "prabin":3333333333,
#     "shashi":4444444444,
#     "sonika":5555555555,
# }
# print(contacts["prasil"])
# contacts["divya"] = 6666666666
# contacts.update({"prashant":7777777777})
# print(contacts)

# contacts["divya"] = 666777777777666
# contacts.update({"prashant":"0000077777"})
# print(contacts)

# del contacts["divya"]
# print(contacts)
# contacts.pop("prashant")
# print(contacts)

# print(contacts.keys())

# # Dict `grades` = subject : marks. Find subject with highest mark.

# grades={
#     "maths": 90,
#     "science": 80,
#     "english": 95, 
#     "history": 100,
# }
# # print(max(grades, key=grades.get))
# print(grades.items())
# """
# suppose highest_mark is of math i.e. 90
# compare this highest_mark with other subjects marks 
# and find the subject with highest mark.
# """

# """
# Dict `stock` = item : quantity. 
# User buys item, reduce quantity 
# by 1 using `.get()` for safe lookup.
# """

# """
# how to merger two dicts in python?

# """
# a = {"a": 1, "b": 2}
# b = {"c": 3, "d": 4}
# b.update(a)

# when to use nested dicts? when you want to store data in a structured way.
user_data = {
   "username": "john_doe",
    "email": "email@email.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "graduation_year": 2020
    }
}
education = user_data["education"]
print(education["major"])  # Output: Computer Science
print(user_data["education"]["major"])


""" 
Restaurant menu dict item :
 price. Ask user for item name, use `.get()` 
 with default "item not available".
"""

menu_items = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 4.99,
}

food_items = ["momo", "burger", "pizza", "samosa"]

print(menu_items.get("pizza"))