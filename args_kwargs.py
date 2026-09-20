

def create_user(**kwargs):
    if "image" in kwargs:
        print("Image not acceptd")


create_user(
    password="124", 
    conform_password="124",
    username="aa",
    email="aa@email.com",
    id=1,
    image="/home/abc.png",
    location="tripuswor",
    age=22
)


# sum all the items bought and return the final total output. 

"""
eg, applle=250, rice=2000, chocolate=500 ---> 2750

calculate_sum(apple=250, rice=2000, chocolate=500)
"""

def calculate_sum_kwargs(**kwargs):
    print(kwargs)
    total_sum = 0
    # for key, value in kwargs.items():
    #     total_sum += value
    return total_sum

def calculate_sum_args(*args):
    print(args)

sum_of_items = calculate_sum_kwargs(apple=250, rice=2000, chocolate=500, mango=400)
sum_of_items = calculate_sum_args(250,2000,500,400)

print(sum_of_items)
