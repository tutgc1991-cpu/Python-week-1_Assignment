# Week 2 Assignment: Simple Bill Calculator

# Ask the user for the price of one item
price = float(input("Enter the price of one item: "))

# Ask the user for the quantity they want
quantity = int(input("Enter the quantity: "))

# Calculate the total cost
total = price * quantity

# Print a friendly summary
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
