
  
import numpy as np

def calculate_statistics(arr1, arr2=None):
    print("--- Statistics Calculation ---")

    mean = np.mean(arr1)
    print(f"Mean: {mean}")

    median = np.median(arr1)
    print(f"Median: {median}")

    std_deviation = np.std(arr1)
    print(f"Standard Deviation: {std_deviation}")

    variance = np.var(arr1)
    print(f"Variance: {variance}")
    if arr2 is not None:
        correlation = np.corrcoef(arr1, arr2)[0, 1]
        print(f"Correlation Coefficient between arr1 and arr2: {correlation}")
    else:
        print("No second array provided for correlation calculation.")

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

calculate_statistics(arr1)

calculate_statistics(arr1, arr2)
