# Create an empty list called my_list
my_list = []
print(f"1. Empty list created: {my_list}")

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"2. After appending 10, 20, 30, 40: {my_list}")

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position (0-based indexing)
print(f"3. After inserting 15 at position 2: {my_list}")

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"4. After extending with [50, 60, 70]: {my_list}")

# Remove the last element from my_list
last_element = my_list.pop()  # pop() removes and returns the last element
print(f"5. After removing last element ({last_element}): {my_list}")

# Sort my_list in ascending order
my_list.sort()
print(f"6. After sorting in ascending order: {my_list}")

# Find and print the index of the value 30 in my_list
try:
    index_30 = my_list.index(30)
    print(f"7. Index of value 30: {index_30}")
except ValueError:
    print("7. Value 30 not found in the list")

# Final state of the list
print(f"\nFinal list: {my_list}")
print(f"Length of list: {len(my_list)}")
