
import numpy as np

one_d_array = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(one_d_array)

print("\nSlicing 1D array (Index 1 to 3):")
print(one_d_array[1:4])

reshaped_2d = one_d_array.reshape(1, 5) 
print("\nReshaped 1D Array to 2D (1x5):")
print(reshaped_2d)

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(two_d_array)

print("\nSlicing 2D array (First 2 rows, all columns):")
print(two_d_array[:2, :])

reshaped_3d = two_d_array.reshape(1, 3, 3)  
print("\nReshaped 2D Array to 3D (1x3x3):")
print(reshaped_3d)

three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3D Array:")
print(three_d_array)

print("\nAccessing 3D Array Element (First block, first row, second column):")
print(three_d_array[0, 0, 1])  

print("\nSlicing 3D Array (First block):")
print(three_d_array[0])
