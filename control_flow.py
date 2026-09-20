"""
if:
elif:
else:

"""

age = 9

if age >= 18:
    print("You are eligible to vote.")
elif age <=15 and age>=10:
    print("You can register only.")
else:
    print("Sorry you cannot vote or register.")


data = [1,3,4,5,5]
lenght_of_data = len(data)

if lenght_of_data <=5:
    data.append("Yes")
else:
    data.append("N0")

print(data)

# nested if else
x = 5

if x > 0:
    if x > 10:
        print("big positive")
    else:
        print("small positive")
else:
    print("negative or zero")

"""
student in clollege get access to canteen in different time interval
"""

time = "1"
canteent_time_up_to_5 = "1"
canteent_time_from_6_to_8 = "1.30"
canteent_time_from_9_to_10 = "2"

if time == canteent_time_up_to_5:
    print("Food available for the class up to 5")
elif time == canteent_time_from_6_to_8:
    print("Food ,,,,")
else:
    print("FOR 9 and 10 student")

