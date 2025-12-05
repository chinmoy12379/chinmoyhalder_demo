a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
operator = input("enter an operator (=,+,-,/,%,//) :")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("divisor can not be zero")
    else:
        print(a / b)
elif operator == "//":
    if b == 0:
        print("divisor can not be zero")
    else:
        print(a // b)
elif operator == "%":
    if b == 0:
        print("divisor can not be zero")
    else:
        print(a % b)
else:
    print("Invalid number")