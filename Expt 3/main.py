
import math  

bs = float(input("Enter the Basic Salary (BS): "))    
da = 0.70 * bs  
ta = 0.30 * bs  
hra = 0.10 * bs    
gross_salary = bs + da + ta + hra

print(f"\n--- Salary Breakdown ---")
print(f"Basic Salary (BS): {bs:.2f}")
print(f"Dearness Allowance (DA): {da:.2f}")
print(f"Travel Allowance (TA): {ta:.2f}")
print(f"House Rent Allowance (HRA): {hra:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")


