student_name = input("Enter student name: ")
student_class = input("Enter class: ")

science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
percentage = total / 300 * 100

print(f"""
=============================
       STUDENT REPORT CARD
=============================
Name:       {student_name}
Class:      {student_class}
Maths:      {maths}
Science:    {science}
English:    {english}
-----------------------------
Total:      {total} / 300
Percentage: {percentage:.2f}%
=============================
""")