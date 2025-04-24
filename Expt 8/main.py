def main():
    while True:
        print("\n--- Even or Odd Checker ---")
        try:
            num = int(input("Enter a number (or type 0 to stop): "))

            if num == 0:
                print("Exiting the program. Goodbye!")
                break

            if num % 2 == 0:
                print(f"{num} is EVEN.")
            else:
                print(f"{num} is ODD.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()

