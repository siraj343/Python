print("Choose a shape to calculate area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)
elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)
elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)
else:
    print("Invalid choice")
