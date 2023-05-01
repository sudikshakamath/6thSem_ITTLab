import sqlite3
conn = sqlite3.connect('test.db')
print("database connected")
conn.commit()

stud_id = int(input("Enter student id: "))
new_cgpa = float(input("Enter new cgpa: "))

conn.execute(
    "update students set cgpa=(?) where id=(?)", (new_cgpa, stud_id,))
cursor = conn.execute(
    "select id,regno,branch,semester,section,cgpa,email from students where id=(?)", (stud_id,))
for row in cursor:
    print("ID = ", row[0])
    print("Reg_No = ", row[1])
    print("Branch = ", row[2])
    print("Semester = ", row[3])
    print("Section = ", row[4])
    print("CGPA = ", row[5])
    print("Email = ", row[6])
print("Operation executed successfully!")
