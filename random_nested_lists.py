import random

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

def multiple_reverse(x, y):
    lst = [[random.randint(x,y) for i in range(x, y)] for i in range(x,y)]
    print(lst[::-1])
    return lst
print(multiple_reverse(x,y))