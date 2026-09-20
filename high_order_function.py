
from functools import reduce

def increment_by_one(value):
    return value / 1

def filter_even_number(number):
    return number%2==0

def reduce_number(num1, num2):
    return num1 * num2




value = map(increment_by_one, [1, 2, 3, 4])
print(list(value))

data = filter(filter_even_number,[1,2,4])
print(list(data))


nums = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc * x, nums)
total = reduce(reduce_number, nums)
print("0000000 ", total)  # 15

# print("ram "*3)

# reduce([1,3,4,5],)


# def add(data):
#     return sum(data)

# def calculator(data,add):
#     return add(data)

# value = calculator([1,3,4], add)
# print(value)


