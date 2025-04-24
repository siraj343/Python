def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print("--- Factorial Calculator ---")
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            fact = factorial(n)
            print(f"Factorial of {n} is {fact}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

main()

