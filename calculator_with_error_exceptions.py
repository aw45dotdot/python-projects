import math

def calculator():
    print("----------Welcome to the calculator app----------")
    while True:
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid input, enter valid number: ")
            continue
            
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, enter valid number: ")
            continue
        
        operator = input("Enter operator(+,-,x,÷): ").strip()
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "x":
                result = num1*num2
            elif operator == "÷":
                result = num1/num2
            else:
                raise ValueError("Invalid operator")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except ValueError:
            print("Invalid operator, enter valid operator(+,-,x,÷)")
            continue
        
        print(f'Result is: {result}')
        calc = input("Continue calculations(y/n)?: ")
        if calc == "n":
            print("Thank you for using calculator")
            break

#calling calculator function
calculator()
