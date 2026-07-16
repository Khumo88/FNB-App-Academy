students = [
    {
        "name": "Khumo",
        "maths": 85,
        "english": 78,
        "science": 90
    },
    {
        "name": "Neo",
        "maths": 65,
        "english": 70,
        "science": 60
    },
    {
        "name": "Lebo",
        "maths": 45,
        "english": 50,
        "science": 40
    },
    {
        "name": "Tumi",
        "maths": 92,
        "english": 88,
        "science": 95
    },
    {
        "name": "Ayanda",
        "maths": 55,
        "english": 62,
        "science": 58
    }
]

results = []

for student in students:
   average = (
     student["maths"] + 
     student["english"] + 
     student["science"]) / 3

   if average >= 75:
     grade = "A"
     status = "Pass"
   elif average >= 60:
     grade = "B"
     status = "Pass"
   elif average >= 50:
     grade = "C"
     status = "Pass"
   else:
     grade = "D"
     status = "Fail"

   results.append({
      "name": student["name"],
      "average": average,
      "grade": grade,
      "status": status
   })

print("CLASS REPORT")
print("_" * 30)

for result in results:
    print("Name:", result["name"])
    print("Average:", round(result["average"], 2))
    print("Grade:", result["grade"])
    print("Status:", result["status"])
    print("-" * 30)

    total_average = 0
    highest_average = 0
    lowest_average = 100

    for result in results:
        total_average += result["average"]

        if result["average"] > highest_average:
            highest_average = result["average"]

        if result["average"] < lowest_average:
            lowest_average = result["average"]

    class_average = total_average / len(results)

print("Class Average:", round(class_average, 2))
print("Highest Average:", round(highest_average, 2))
print("Lowest Average:", round(lowest_average, 2))
while True:
   search = input("Enter a student's name to search (or type 'quit' to exit): ")

   if search.lower() == "quit":
         print("Goodbye!")
         break
   
   found = False

   for result in results:
         if result["name"].lower() == search.lower():
                print("=============================")
                print("Name:", result["name"])
                print("Average:", round(result["average"], 2))
                print("Grade:", result["grade"])
                print("Status:", result["status"])
                print("=============================")
                found = True
                break
         
         if not found:
                print("Student not found.")