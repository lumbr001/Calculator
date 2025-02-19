#calculator program
#addition, subtraction, multiplication, division, average, probability, percentage, remainder, power, square, cube    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
    
def average(a, b):
    return (a + b) / 2  

def probability(a, b):
    return (a / b) * 100 

def percentage(a, b):
    return (a / b) * 100

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a ** 2

def cube(a):    
    return a ** 3

#function to get number from user

def get_number(prompt):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Calculator")
    print("This is a basic calculator program that can perform the following operations:")
    print("Operations: +, -, *, /, average, probability, percentage, remainder, power, square, cube")
    print("Enter 'exit' to quit.\n")

    while True:
        operation = input("Enter operation (+, -, *, /, average, probability, percentage, remainder, power, square, cube) or 'exit': ").strip()
        
        if operation.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        if operation not in ['+', '-', '*', '/', 'average', 'probability', 'percentage', 'remainder', 'power', 'square', 'cube']:
            print("Invalid operation. Please choose from +, -, *, /, average, probability, percentage, remainder, power, square, cube.")
            continue
        
        num1 = get_number("Enter first number: ")
        
        if operation in ['square', 'cube']:
            num2 = None
        else:
            num2 = get_number("Enter second number: ")

        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == 'average':
                result = average(num1, num2)
            elif operation == 'probability':
                result = probability(num1, num2)
            elif operation == 'percentage':
                result = percentage(num1, num2)
            elif operation == 'remainder':
                result = remainder(num1, num2)
            elif operation == 'power':
                result = power(num1, num2)
            elif operation == 'square':
                result = square(num1)
            elif operation == 'cube':
                result = cube(num1)
            
            print(f"\nResult: {result}\n")
        
        except ValueError as e:
            print(f"\nError: {e}\n")
        
        another = input("Perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
