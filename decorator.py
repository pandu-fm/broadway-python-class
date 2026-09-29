# def able_to_access_data(permission="READ"):
#     def login_required(func):
#         def inner_func(*args, **kwargs):
#             if permission == "READ":
#                 return func(*args, **kwargs)
#             raise ValueError("Not authenticated.")
#         return inner_func
#     return login_required

# def check_permission(permission_name = "READ"):
#     return "jj"

# @able_to_access_data(permission="READ")
# def payment(name, amount):
#     print("User ", name , " spent total ", amount)


# @able_to_access_data(permission="WRITE")
# def genreate_bill(name, amount):
#     print("User ", name , " spent total ", amount)

# payment("e", 2999)
# genreate_bill("e", 2999)

# inner_func = login_required(payment)
# print(inner_func("2", 2000))

import time
from datetime import datetime
from functools import wraps

def logger(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print(f"Function '{func.__name__}' execution started at", datetime.now())
        start = time.perf_counter()
        data = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Function '{func.__name__}' execution completed in {elapsed:.4f}s")
        return data
    return inner_func


@logger
def claculate_amount(*args,  **kwargs):
    pass

@logger
def validate_data(*args, **kwargs):
    pass

claculate_amount()
# validate_data()