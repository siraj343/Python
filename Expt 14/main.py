def divide_numbers():
    print("--- Division with Exception Handling ---")
    
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")

divide_numbers()
