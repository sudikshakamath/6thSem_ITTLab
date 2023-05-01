import sqlite3
conn = sqlite3.connect('test.db')
print("connected to db successfully")
# conn.execute('''CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50),SALARY REAL);''')
# print("table created successfully")
# conn.commit()
# conn.execute(
#     "INSERT INTO COMPANY VALUES(2,'Allen',25,'Texas',30000.00)")
# conn.execute(
#     "INSERT INTO COMPANY VALUES(3,'Teddy',28,'Norway',15000.00)")
# conn.execute(
#     "INSERT INTO COMPANY VALUES(4,'Mark',25,'Seattle',62000.00)")
# conn.commit()

conn.execute("update company set salary = 250000.00 where id=1")
conn.commit()
print("total number of rows updated: ", conn.total_changes)
cursor = conn.execute("select id,name,address,salary from company")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Address = ", row[2])
    print("Salary = ", row[3])
print("\n")
print("operation done successfully!")
