import sqlite3
conn = sqlite3.connect('test.db')
print("database connected")

conn.commit()
conn.execute('''create table students(id int primary key not null, regno int not null, branch text not null,semester int not null, section char(2),cgpa real, email text not null);''')
print("table created successfully!")

conn.execute(
    "insert into students values(1, '2002', 'CSE', 5, 'B', 8.9, 'xyz@gmail.com')")
conn.execute(
    "insert into students values(2, '2003', 'IT', 6, 'A', 9.0, 'abz@gmail.com')")
conn.execute(
    "insert into students values(3, '2004', 'EEE', 7, 'C', 9.6, 'abc@gmail.com')")
conn.execute(
    "insert into students values(4, '2005', 'ECE', 5, 'A', 9.3, 'def@gmail.com')")
conn.commit()
print("records inserted successfully!")

cursor = conn.execute(
    "select id,regno,branch,semester,section,cgpa,email from students order by cgpa asc")
for row in cursor:
    print("ID = ", row[0])
    print("Reg_No = ", row[1])
    print("Branch = ", row[2])
    print("Semester = ", row[3])
    print("Section = ", row[4])
    print("CGPA = ", row[5])
    print("Email = ", row[6])
print("Operation executed successfully!")


# path to the db: .cd /Users/kushalpendekanti/Documents/ITT_Lab/Lab7/
