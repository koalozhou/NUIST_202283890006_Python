# Print studentNames list
# Author: Renjie Zhou
# Using list

# Print each name plus last name "Evans"
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
for name in studentNames:
    print(f"{name} Evans")

# add a new name
new_name = input("Enter a new name to add: ")
studentNames.append(new_name)

# reprint the updated list
print("\nUpdated list with Evans:")
for name in studentNames:
    print(f"{name} Evans")
