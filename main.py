def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

num1 = int(input("enter the number 1 :"))
num2 = int(input("enter the number 2 :"))

print("sum :", add(num1, num2))
print("diffrence :", subtract(num1, num2))
print("product :", multiply(num1, num2))
print("quotient :", divide(num1, num2))