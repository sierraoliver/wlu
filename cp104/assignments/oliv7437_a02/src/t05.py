"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# user inputs
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))

wall_height = float(input("Wall height (m): "))

concrete_cost = float(input("Cost of concrete ($/m^3): "))
brick_cost = float(input("Cost of bricks ($/m^2): "))


# calculations
concrete_needed = foundation_length * foundation_width * foundation_height
concrete_cost_needed = concrete_cost * concrete_needed

bricks_needed = (foundation_length * wall_height * 2) + \
    (foundation_width * wall_height * 2)
brick_cost_needed = brick_cost * bricks_needed

total_cost = concrete_cost_needed + brick_cost_needed

# printing
print(f"""
Concrete needed for foundation (m^3): {concrete_needed:.2f}
Cost of concrete: ${concrete_cost_needed:.2f}
Bricks needed for wall (m^2): {bricks_needed:.2f}
Cost of bricks: ${brick_cost_needed:,.2f}")
Total cost: ${total_cost:,.2f}
""")
