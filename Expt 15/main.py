import pdb

def calculate_area(radius):
  
    area = 3.14159 * radius ** 2
    radius = 0  
    return area

def main():
    radius = input("Enter the radius: ")  
    try:
        radius = float(radius)  
        area = calculate_area(radius)
        print(f"The area of the circle is: {area}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
