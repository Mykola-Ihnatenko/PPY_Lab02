# Task 1
"""line = input("Enter a series of space-separated integers: ")
x = [int(num) for num in line.split(" ")]
print("Sorted list:", sorted(x))"""

# Task 2
"""line = input("Enter a series of space-separated integers: ")
List = [int(num) for num in line.split(" ")]
Tuple = (tuple(sorted(List)))
print("Sorted list:", sorted(List))
print("Sorted tuple:", Tuple)"""

# Task 3
"""line = input("Enter a series of space-separated integers: ")
List = [int(num) for num in line.split(" ")]
List.append(-9999)
List.insert(1, 10)
List.remove(-9999)
Tuple = (tuple(sorted(int(num) for num in line.split(" "))))
try:
    Tuple.append(-9999)
    Tuple.insert(1, 1111111)
    Tuple.remove(-9999)
except AttributeError:
    print("\nTuples are immutable and cannot be modified.\n")
print("Sorted list:", sorted(List))
print("Sorted tuple:", Tuple)"""

#Task 4
# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = sorted([int(num) for num in input_numbers.split(" ")])
numbers_tuple = (tuple(sorted(int(num) for num in input_numbers.split(" "))))

# Manipulate List
# Append 10 to the list
numbers_list.append(10)
# Insert 20 at index 2
numbers_list.insert(2, 20)
# Remove the element 8
numbers_list.remove(8)

# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
set1 = set(numbers_list)
# Union
set_union = set1.union({1, 10, 11, 12})
# Intersection
set_intersection = set1.intersection({1, 2, 3, 4, 5, 8})
# Difference
set_difference = set1.difference({1, 2, 3, 4, 5})

# Dictionary Operations
numbers_dict = {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
numbers_dict[99] = -99
numbers_dict.update({9999: -1111})
# Delete an existing key-value pair
numbers_dict.pop(5)
del numbers_dict[2]
numbers_dict.popitem()

# Print Output
print("Modified list:", numbers_list)
print("Tuple remains unchanged:", numbers_tuple)
print("Union of set:", set_union)
print("Intersection of set:", set_intersection)
print("Difference of set:", set_difference)
print("Updated Dictionary:", numbers_dict)
