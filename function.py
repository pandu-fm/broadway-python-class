""" python function """

# def say_something():
#     print("I am inside function.")
#     return "HI"

# data = say_something()
# print(data)

"""

Email to be sent during : Forget password, reset password, send_recept_to_user_via_mail

"""

# def send_mail(email, body):
#     print(f"sending mail to {email}. Using {body}")

# # forget password
# body = "Hi Tomorroew is holiday"
# send_mail("prabin@gmail.con", body)

# # reset password
# body = "Hi Come to office at 8 o clock"
# send_mail("abc@gmail.con",body)

# # send_recept_to_user_via_mail
# # send_mail()


# to add two number
# def add_two_number(a, b, c=20):
#     return a+b

# add_two_number(1, "dsdd")

# add_two_number(100, 4)
# add_two_number(1,1)
# add_two_number(1)


# def calculate_amount(data, gloabl_nepal_vat_rule=20):
#     vat_amount = (vat/100)*sum(data)
#     return sum(data)+vat_amount

# print(calculate_amount([100, 2000, 10, 40]))
# print(calculate_amount([10, 40]))

# def args_argument(number1, number2, *data):
#     print(data)
#     print(number1, number2)

# args_argument(1,3,4,5,2345,6)

# def keyworad_arguments(age,**data):
#     print(data)


# keyworad_arguments(name="ram", age=20, address="Ktm")



# a,*b = (1,3,4,5)

# print(a, b)


# def print_marksheet(class_name, student_name, roll_number, marks):

#     total = sum(marks.values())
#     average = total / len(marks)

#     print(f"Class: {class_name}")
#     print(f"Name: {student_name}")
#     print(f"Roll Number: {roll_number}")
#     print("Marks:")
#     for subject, score in marks.items():
#         print(f"  {subject}: {score}")
#     print(f"Total: {total}")
#     print(f"Average: {average:.2f}")

# print_marksheet("One", "raju",1, {"social": 40, "math": 70})
# print_marksheet("One", "raju",1, {"social": 40, "math": 70})



# def welcome_customer(name, greet="morning"):

#     if time>13 amd < 5:
#         greet = "afternoon"
#     else:
#         greet = "good night"

#     print(f"Hello {name}, good {greet}")
#     print("Your romme is this ")

# welcome_customer("Ram", "morning")
# welcome_customer("Prabin", "good evening.")



def finger_print():
    pass

def face_scan():
    pass

def eye_scan(eye_coordinate):
    """
    eye_coordinate: this is the corrdinate of human eye
    """
    pass

# input -> process -> output


# lambda function
(lambda number : number + 10)(77)

# scope
name = "test"
print(name)


def play_music():

    global play

    play = True

    print(play, name)

play_music()
print(play)

""" Create a function called check password that will have default value as 
orginal password. You need to provide different password on calling the function
if provided value match with default return True else return False. It will accept
provided_pass, orginal_pass as parameter. orginal_pass is default value in this case."""


def check_password(provided_pass, orginal_pass="pass"):
    if orginal_pass == provided_pass:
        return True
    return False

"""
Write a function calculate_discount(price):
Price >= 5000 → 20% discount
Price >= 2000 and <=5000 → 10% discount
Otherwise → no discount
"""

func_ = lambda pass1, pass2="p": pass1 == pass2
print("--------", func_("pjk"))
