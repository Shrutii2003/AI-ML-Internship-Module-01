# Python Lists Practice

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)

# Accessing list elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Adding an item
fruits.append("Grapes")
print("After adding:", fruits)

# Removing an item
fruits.remove("Banana")
print("After removing:", fruits)

# Loop through a list
print("\nAll fruits:")

for fruit in fruits:
    print(fruit)

# List of numbers
numbers = [10, 20, 30, 40, 50]

print("\nNumbers:", numbers)
print("Total:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
