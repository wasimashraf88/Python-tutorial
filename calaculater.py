bill = 20
tip_percentage = 0.15
tax_percentage = 0.067

tip = bill * tip_percentage
tax = bill * tax_percentage
print(f"Tip: {tip}")
print(f"Tax: {tax}")

total = tip + bill + tax
print(f"Total: {total}")