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
line = input("Enter a series of space-separated integers: ")
List = [int(num) for num in line.split(" ")]
List.append(-9999)
List.insert(1, 1111111)
List.remove(-9999)
Tuple = (tuple(sorted(int(num) for num in line.split(" "))))
try:
    Tuple.append(-9999)
    Tuple.insert(1, 1111111)
    Tuple.remove(-9999)
except AttributeError:
    print("\nTuples are immutable and cannot be modified.\n")
print("Sorted list:", sorted(List))
print("Sorted tuple:", Tuple)
