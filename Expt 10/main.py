def is_prime(n): 
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

def main():
    print("--- Prime Number Checker ---")
    try:
        num = int(input("Enter a positive integer: "))
        if is_prime(num):
            print(f"{num} is a PRIME number.")
        else:
            print(f"{num} is NOT a prime number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

main()
