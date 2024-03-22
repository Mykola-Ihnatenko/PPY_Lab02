#Task 8

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

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = {index: value for index, value in enumerate(numbers_list)}
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = {value: value**2 for value in numbers_tuple}
set_to_list = list(set1)
set_to_tuple = tuple(set1)
set_to_dict = {value: value**3 for value in set1}
dict_to_list = sorted(numbers_dict.keys())
dict_to_tuple = tuple(sorted(numbers_dict.keys()))
dict_to_set = set(numbers_dict.values())

# Print Output
print("List to Tuple:", list_to_tuple)
print("List to Set:", list_to_set)
print("List to Dictionary:", list_to_dict)
print("Tuple to List:", tuple_to_list)
print("Tuple to Set:", tuple_to_set)
print("Tuple to Dictionary:", tuple_to_dict)
print("Set to List:", set_to_list)
print("Set to Tuple:", set_to_tuple)
print("Set to Dictionary:", set_to_dict)
print("Dictionary to List:", dict_to_list)
print("Dictionary to Tuple:", dict_to_tuple)
print("Dictionary to Set:", dict_to_set)

with open("output.txt", "w") as file:
    file.write("Original Input: " + input_numbers + "\n")
    file.write("List to Tuple: " + str(list_to_tuple) + "\n")
    file.write("List to Set: " + str(list_to_set) + "\n")
    file.write("List to Dictionary: " + str(list_to_dict) + "\n")
    file.write("Tuple to List: " + str(tuple_to_list) + "\n")
    file.write("Tuple to Set: " + str(tuple_to_set) + "\n")
    file.write("Tuple to Dictionary: " + str(tuple_to_dict) + "\n")
    file.write("Set to List: " + str(set_to_list) + "\n")
    file.write("Set to Tuple: " + str(set_to_tuple) + "\n")
    file.write("Set to Dictionary: " + str(set_to_dict) + "\n")
    file.write("Dictionary to List: " + str(dict_to_list) + "\n")
    file.write("Dictionary to Tuple: " + str(dict_to_tuple) + "\n")
    file.write("Dictionary to Set: " + str(dict_to_set) + "\n")

with open("output.txt", "r") as file:
    num_lines = sum(1 for line in file)
    print("Number of lines in the file:", num_lines)

    file.seek(0)
    for line in file:
        if "Original Input" in line:
            print("Original Input found:", line.strip())

with open("output.txt", "a") as file:
    file.write("here\n")

    # Count the number of lines in the file
    with open("output.txt", "r") as file:
        num_lines = sum(1 for line in file)
        print("Number of lines in the file:", num_lines)

    # Count the number of integers in the file
    with open("output.txt", "r") as file:
        all_numbers = file.read().split()
        num_integers = sum(1 for num in all_numbers if num.isdigit())
        print("Number of integers in the file:", num_integers)

    # Add all integers in the file (sum)
    with open("output.txt", "r") as file:
        all_numbers = file.read().split()
        integers_sum = sum(int(num) for num in all_numbers if num.isdigit())
        print("Sum of all integers in the file:", integers_sum)

    # Modify the content of the file
    with open("output.txt", "a") as file:
        file.write("\nFile content modified.")


# Task 9
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

largest_integer = None
with open("output.txt", "r") as file:
    for line in file:
        if line.startswith("Original Input"):
            largest_integer = max(map(int, line.split()[-1].split(",")))
            break

if largest_integer is None:
    print("Error: Largest integer not found in the file.")
    exit()

prime_numbers = [num for num in range(2, largest_integer + 1) if is_prime(num)]

print("List of prime numbers up to", largest_integer, ":", prime_numbers)

prime_sum = sum(prime_numbers)

largest_prime = max(prime_numbers)
smallest_prime = min(prime_numbers)

largest_integer_prime = is_prime(largest_integer)

with open("prime_numbers.txt", "w") as file:
    file.write("List of prime numbers: " + str(prime_numbers) + "\n")
    file.write("Sum of prime numbers: " + str(prime_sum) + "\n")
    file.write("Largest prime number: " + str(largest_prime) + "\n")
    file.write("Smallest prime number: " + str(smallest_prime) + "\n")
    file.write("Is the largest integer prime?: " + ("Yes" if largest_integer_prime else "No") + "\n")
