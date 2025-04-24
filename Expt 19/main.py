import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

print("--- Element-wise Operations ---")

addition = array1 + array2
print("Addition:")
print(addition)

subtraction = array1 - array2
print("\nSubtraction:")
print(subtraction)

multiplication = array1 * array2
print("\nMultiplication:")
print(multiplication)

try:
    division = array1 / array2
    print("\nDivision:")
    print(division)
except ZeroDivisionError:
    print("Error: Division by zero.")

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

print("\n--- Dot and Cross Product ---")

dot_product = np.dot(vector1, vector2)
print("Dot Product:")
print(dot_product)

cross_product = np.cross(vector1, vector2)
print("\nCross Product:")
print(cross_product)
