# Task 1
"""line = input("Enter a series of space-separated integers: ")
x = [int(num) for num in line.split(" ")]
print("Sorted list:", sorted(x))"""

# Task 2
line = input("Enter a series of space-separated integers: ")
List = [int(num) for num in line.split(" ")]
Tuple = (tuple(sorted(List)))
print("Sorted list:", sorted(List))
print("Sorted tuple:", Tuple)

