import sqlite3

# Create a database connection
conn = sqlite3.connect('test.db')

# Create a table for student data
conn.execute('''CREATE TABLE students1
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             SUBJECT1 INT NOT NULL,
             SUBJECT2 INT NOT NULL,
             SUBJECT3 INT NOT NULL,
             SUBJECT4 INT NOT NULL,
             SUBJECT5 INT NOT NULL);''')

# Insert data into the table
conn.execute("INSERT INTO students1 (ID, NAME, SUBJECT1, SUBJECT2, SUBJECT3, SUBJECT4, SUBJECT5) \
              VALUES (1, 'John', 85, 90, 92, 88, 95)")
conn.execute("INSERT INTO students1 (ID, NAME, SUBJECT1, SUBJECT2, SUBJECT3, SUBJECT4, SUBJECT5) \
              VALUES (2, 'Jane', 92, 94, 90, 95, 87)")
conn.execute("INSERT INTO students1 (ID, NAME, SUBJECT1, SUBJECT2, SUBJECT3, SUBJECT4, SUBJECT5) \
              VALUES (3, 'Bob', 78, 85, 82, 90, 88)")
conn.execute("INSERT INTO students1 (ID, NAME, SUBJECT1, SUBJECT2, SUBJECT3, SUBJECT4, SUBJECT5) \
              VALUES (4, 'Alice', 95, 92, 90, 94, 98)")

# Retrieve data from the table
cursor = conn.execute(
    "SELECT ID, NAME, SUBJECT1, SUBJECT2, SUBJECT3, SUBJECT4, SUBJECT5 FROM students1")
for row in cursor:
    # Compute the total marks
    total_marks = sum(row[2:])

    # Grade the student based on the total marks
    if total_marks >= 450:
        grade = 'A'
    elif total_marks >= 400:
        grade = 'B'
    elif total_marks >= 350:
        grade = 'C'
    elif total_marks >= 300:
        grade = 'D'
    else:
        grade = 'F'

    # Display the results
    print(f"Student ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Total marks: {total_marks}")
    print(f"Grade: {grade}")
    print("---------------")

# Close the connection
conn.close()
