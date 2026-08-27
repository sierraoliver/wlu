"""
-------------------------------------------------------
Lab 7, Task 8
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports
from functions import budget

available = float(input("Money currently available: "))

expenses, balance, status = budget(available)

print(f"""
Total Expenses: {expenses:.2f}
Remaining Balance: {balance:.2f}
Status: {status}
""")
