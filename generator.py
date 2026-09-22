

def get_names():
    yield "a"
    yield "b"
    yield "C"
    # return ["a", "b", "c"]

names = get_names()
# print(names)

print(next(names))
print(next(names))
print(next(names))
# print(next(names))  # raises StopIteration, generator exhausted

# re-create generator to loop over it
# for name in get_names():
#     print(name)

# def read_csv():
#     return [csv_data] # 1 gb

# def read_csv():
#     yield csv # one line at time


# user generator to print students one by one

# students = ["H", "K", "l", "m", "P"]

"""
Write a functional program that gives multiplication of 2 
using the concept of generator. """

def multiplication_of(multiplication_of=1):
    # result = []
    for num in range(1,11):
        # result.append(multiplication_of*num)
        yield multiplication_of * num
    # return result

data = multiplication_of(2)
# print(data)
print(next(data))
# print(next(data))

for num in data:
    print(num)



def gethki():
    students = ["H","k","l","m","p"]
    for i in students:
        yield i
        # j =(len(students))
        # return j
 
for data in gethki():
    print(data)
 
# k =1
# while k < j:
#     print(next(gethki()))
#     k +=1
