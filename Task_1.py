# Task 1:
# Calculator
""" Create a basic calculator that can perform basic arotmatic operations such as Addition
    Substraction, Multiplication, Division using functions."""

def Addition(a,b):
    return a + b
def Substraction(a,b):
    return a - b
def Multiplication(a,b):
    return a * b
def Division(a,b):
    return a / b
print("Select the Operation: ")
print("1.Addition\n"\
      "2.Substraction\n"\
      "3.Multiplication\n"\
      "4.Division\n")
Operation = int(input("Enter your choice of Operation 1/2/3/4: "))
a = float(input("Enter the First Number: "))
b = float(input("Enter the Second Number: "))
print("\n***Calcaulate***")
if Operation == 1:
    print(a," + ",b," = ",Addition(a,b))
elif Operation == 2:
    print(a," - ",b," = ",Substraction(a,b))
elif Operation == 3:
    print(a," * ",b," = ",Multiplication(a,b))
elif Operation == 4:
    print(a," / ",b," = ",Division(a,b))
else:
    print("Invalid")