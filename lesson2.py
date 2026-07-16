# Username and Message Formatter

# Get username input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Enter a short bio").strip()

# Create username
username = (first_name[0] + last_name).lower()

# Display full name in Title Case
full_name = f"{first_name} {last_name}".title()

# Count characters in the bio
bio_length = len(bio)

# Replace "I am" with "I'm"
bio = bio.replace("I am", "I'm")

# Display results
print(f"\nFull Name: {full_name}")
print(f"Username: {username}")
print(f"Bio: {bio}")
print(f"Bio Length: {bio_length} characters")

# Secure Password Hint Tool

# Ask the user for their password
password = input("Enter your secret password:").strip()

# Get the first and last letters
first_letter = password[0]
last_letter = password[-1]

# Display the hint
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}.")

# Lesson 2 completed