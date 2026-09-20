""" 
1. You have users = ['Ram', 'Sita']. 
A new user 'Hari' registers. Which 
list method should you use? 
Write the code.
"""
users = ['Ram', 'Sita']
print("Initial users:", users)
# using insert
users.insert(1, 'Hari')
print("Users after adding Hari:", users)

# using append
users.append('gopal')
print("Users after appending gopal:", users)

# using extend
users.extend(['Maya', 'Ravi', 1, 3, 4])
print("Users after extending with Maya and Ravi:", users)

# delete the last user
users.pop()
print("Users after popping the last user:", users)

# using remove
users.append("Hari")
print("Users after adding Hari again:", users)
users.remove('Hari')
print("Users after removing Hari:", users)
# users.clear()
# print("Users after clearing the list:", users)
users.pop(0)
print("Users after popping the first user:", users)

matrix_list = [
    [1,2], # 0 index
    [3,4], # 1 index
]

matrix_list[0].append(5)
print("Matrix", matrix_list)


random_numbers = [1,20,2,5,7]
random_numbers.sort()
print("Random numbers:",random_numbers)