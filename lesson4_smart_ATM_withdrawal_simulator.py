# Fixed bank balance
balance = 500.00

# Ask the user for the withdrawal amount
withdrawal = float(input("Enter the amount you want to withdraw (R): "))

# Check the withdrawal amount
if withdrawal > 0 and withdrawal <= balance:
    balance = balance - withdrawal
    print(f"Withdrawal successful! Your new balance is: R{round(balance, 2)}")

elif withdrawal <= 0:
    print("Invalid amount! You must withdraw more than R0")

else:
    print("Declined! Insufficient funds.")