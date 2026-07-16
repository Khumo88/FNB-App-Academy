# Calculating the tip

bill = float(input("Enter the bill: R"))
tip = 0.15 # Written in decimal

val_tip = bill * tip
total_cost = bill + val_tip

print(f"Here is the tip: {val_tip}")
print(f"Here is the tip: {round(val_tip, 2)} rounded")

print(f"Here is the total_cost: {total_cost}")
print(f"Here is the total_cost: {round(total_cost, 2)} rounded")