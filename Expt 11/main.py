def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("--- Simple Calculator ---")
    
    while True:
        try:
            # Take user input
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Perform the operation
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            
            print(f"Result: {result}")
            
            # Ask to continue or not
            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                print("Exiting calculator. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
