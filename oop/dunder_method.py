class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("Adding.")
        return self.value + other.value

    def __eq__(self, other):
        return self.value > other.value

num1 = Number(10)
num2 = Number(20)

print(num1 + num2)
# print(1+2)
# print("a "+"n")
# print(num1>num2)