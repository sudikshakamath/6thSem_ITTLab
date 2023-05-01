import sqlite3
conn = sqlite3.connect('test.db')
print("database connected")
conn.commit()

conn.execute(
    '''create table registration (id text primary key not null,pass text not null);''')
conn.commit()
print("table created successfully!")

conn.execute("insert into registration values ('kushal','admin')")
conn.execute("insert into registration values ('sudi','admin1') ")
conn.commit()

ids = input("Enter username: ")
password = input("Enter password: ")

flag = 0
cursor = conn.execute("select id,pass from registration")
for row in cursor:
    if(row[0] == ids and row[1] == password):
        print("welcome\n")
        flag = 1

if(flag == 0):
    print("access denied!")
