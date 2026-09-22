# username = input("Enter your name : ")

# print(username)

# # comprehesion
# even_number = [num for num in range(1,21) if num%2==0]


# even_number = []

# for num in range(1,21):
#     if num % 2 == 0:
#         even_number.append(num)

# print(even_number)
# print(even_number)


user_results = [
    {
        "name": "Hari",
        "study": "class 2"
    },
    {
        "name": "Rajesh",
        "study": "class 3"
    }
]

passed_student = [
    user_result for user_result in user_results if user_result.get("passed")]
print(passed_student)


passed_students = []
failed_students = []
for r in user_results:
    if r.get("passed"):
        passed_students.append(r)
    else:
        failed_students.append(r)

# dictionary comprehesion

result_map = {result["name"]: result["passed"] for result in user_results}
print(result_map)

user_info_dict = {}
for result in user_results:
    user_info_dict.update(
        {
            result.get("name"): result.get("study"),
        }
    )

print(user_info_dict)