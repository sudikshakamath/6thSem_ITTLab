import sqlite3
conn = sqlite3.connect('test.db')
print("database connected")
conn.commit()

regno = int(input("Enter regno: "))

cursor = conn.execute(
    "select id,regno,branch,semester,section,cgpa,email from students where regno =(?)", (regno,))
for row in cursor:
    print("ID = ", row[0])
    print("Reg_No = ", row[1])
    print("Branch = ", row[2])
    print("Semester = ", row[3])
    print("Section = ", row[4])
    print("CGPA = ", row[5])
    print("Email = ", row[6])
print("Operation executed successfully!")
