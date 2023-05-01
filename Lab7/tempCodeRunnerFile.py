conn.execute(
    '''create table registration (id text primary key not null,pass text not null);''')
conn.commit()
print("table created successfully!")

conn.execute("insert into registration values ('kushal','admin')")
conn.execute("insert into registration values ('sudi','admin1') ")
conn.commit()