# Multi-Functional Calculator

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Basic arithmetic
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("\n===== Calculator Results =====")
print(f"Addition: {round(addition, 2)}")
print(f"Subtraction: {round(subtraction, 2)}")
print(f"Multiplication: {round(multiplication, 2)}")

# Division, floor division, and modulus
if num2 != 0:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
    
    print(f"Division: {round(division, 2)}")
    print(f"Floor Division: {round(floor_division, 2)}")
    print(f"Modulus: {round(modulus, 2)}")
else:
    print("Cannot divide by zero.")