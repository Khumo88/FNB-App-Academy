# Student Grader Classifier

# Collect learner information
name = input("Enter the student's name: ")

subject1 = float(input("Enter Subject 1 mark: "))
subject2 = float(input("Enter Subject 2 mark: "))
subject3 = float(input("Enter Subject 3 mark: "))

# Calculate average
average = (subject1 + subject2 + subject3) / 3

# Determine grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

#Determine pass/fail
if average >= 50:
    status = "PASS"
else:
    status = "FAIL"

# Display report card
print("\n===== STUDENT REPORT CARD =====")
print(f"Learner Name: {name}")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")

# Intervention flags
print("\nNeeds Intervention:")

if subject1 < 40:
    print("Subject 1")

if subject2 < 40:
    print("Subject 2")

if subject3 < 40:
    print("Subject 3")

if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print("None")

print("======================================")