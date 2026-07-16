#  South African Fuel Cost Calculator

# Get input from the user
kilometers = float(input("How many kilometres will you drive? "))
petrol_price = float(input("Enter the petrol price per litre (R): "))

# Calculate fuel needed
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Display the results
print(f"\n===== Fuel Cost Calculator =====")
print(f"Distance: {kilometers} km")
print(f"Fuel Needed: {round(liters_needed, 2)} litres")
print(f"Petrol Price: R{round(petrol_price, 2)}")
print(f"Total Fuel Cost: R{round(total_cost, 2)}")