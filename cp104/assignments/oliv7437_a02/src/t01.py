"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Constants
TAX_RATE = 0.185

total_sales = float(input("Enter the total sales: $"))
print()

tax = total_sales * TAX_RATE

print(f"""
Projected Tax Report
--------------------------
Total sales:   $ {total_sales:,.2f}
Annual tax:    % {TAX_RATE*100:,.2f}
--------------------------
Tax:           $  {tax:,.2f}
""")
