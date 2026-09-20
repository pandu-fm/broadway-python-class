students = ['s',1, 2, 3, 4, 5]

#update the value of the list at index 2   
students[2] = "Alice"

# insert at last
students.append("Bob")

# insert at index 0
# students.insert(0, "Charlie")
students.insert(8, "s")

students.remove("s")

print("orginal:", students)

# delete the 2 position element of the list
students.pop(2)
# delete the last element of the list
students.pop()

print("After pop:", students)

# students.clear()
# print("After clear:", students)
 
students.extend(["r", "b", "b"])
print("After extend:", students)


# string_and_numbers = ["Hello", 1, 2, 3, 4, 5]
# sting_numbers_and_boolean = ["Hello", 1, 2, 3, 4, 5, True, False]
# string_and_numbers_and_list = [
#     "Hello",1, 2, 3, 4, 5, [1, 2, 3, 4, 5]
# ]
# list_with_dictionary = [
#     {"name": "Alice", "age": 25},
#     {"name": "gopal", "age": 22}
# ]

# list_with_tuple = [             
#     ("Alice", 25),
#     ("gopal", 22)
# ]

