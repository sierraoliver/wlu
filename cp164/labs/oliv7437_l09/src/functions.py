"""
-------------------------------------------------------
Lab 9, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print(f"Hash     Slot Key")
    print(f"-------- ---- --------------------")

    for x in range(len(values)):
        value = values[x]
        text = f"{value.key()}"
        h_value = hash(value)
        key = h_value % slots
        print(f"{h_value:>9d} {key:>4d} {text:<20s}")

    return
