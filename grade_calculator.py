student_name = input("Enter Student Name: ")
marks = int(input("Enter Marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid Marks! Enter between 0 and 100.")
if marks >= 90:
    grade = "A"
    message = "Excellent! Keep it up!"
elif marks >= 80:
    grade = "B"
    message = "Very Good!"
elif marks >= 70:
    grade = "C"
    message = "Good Job!"
elif marks >= 60:
    grade = "D"
    message = "Keep Improving!"
else:
    grade = "F"
    message = "Need More Practice!"

print("\n----- RESULT -----")
print("Student:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)