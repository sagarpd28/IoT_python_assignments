# -------------------------------
# Function to calculate total marks
# -------------------------------
def calculate_total(student):
    return student["Maths"] + student["VLSI"] + student["Python"]


# -------------------------------
# Student Data (Example)
# -------------------------------
students = [
    {"name": "Anil", "Maths": 78, "VLSI": 88, "Python": 67},
    {"name": "Megha", "Maths": 92, "VLSI": 81, "Python": 95},
    {"name": "Rohit", "Maths": 65, "VLSI": 72, "Python": 70},
    {"name": "Suma", "Maths": 85, "VLSI": 90, "Python": 80}
]


# -------------------------------
# 1. Add total marks for each student
# -------------------------------
for student in students:
    student["total"] = calculate_total(student)


# -------------------------------
# 2. Sort by total marks (descending)
# -------------------------------
students_sorted = sorted(students, key=lambda x: x["total"], reverse=True)


# -------------------------------
# 3. Identify topper and lowest performer
# -------------------------------
topper = students_sorted[0]
lowest = students_sorted[-1]


# -------------------------------
# 4. Subject-wise highest scores
# -------------------------------
highest_maths = max(students, key=lambda x: x["Maths"])
highest_vlsi = max(students, key=lambda x: x["VLSI"])
highest_python = max(students, key=lambda x: x["Python"])


# -------------------------------
# 5. Save structured report to a text file
# -------------------------------
report = []

report.append("===== STUDENT REPORT =====\n\n")
report.append("Sorted Student List (High → Low Total):\n")

for s in students_sorted:
    report.append(f"{s['name']}: Maths={s['Maths']}, VLSI={s['VLSI']}, Python={s['Python']}, Total={s['total']}\n")

report.append("\nTopper:\n")
report.append(f"{topper['name']} with {topper['total']} marks\n")

report.append("\nLowest Performer:\n")
report.append(f"{lowest['name']} with {lowest['total']} marks\n")

report.append("\nSubject-wise Highest Scorers:\n")
report.append(f"Maths: {highest_maths['name']} ({highest_maths['Maths']})\n")
report.append(f"VLSI: {highest_vlsi['name']} ({highest_vlsi['VLSI']})\n")
report.append(f"Python: {highest_python['name']} ({highest_python['Python']})\n")

# Write to file
with open("student_report.txt", "w") as file:
    file.writelines(report)

print("Report generated successfully in 'student_report.txt'")
