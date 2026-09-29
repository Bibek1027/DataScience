num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation: +, -, *, /")

operator = input("Enter operation: ")

if operator == "+":
    result = num1 + num2
    print("The sum is:", result)

elif operator == "-":
    result = num1 - num2
    print("The difference is:", result)

elif operator == "*":
    result = num1 * num2
    print("The product is:", result)

elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print("The result is:", result)

else:
    print("Invalid operator.")