import sqlite3

# Create a database connection
conn = sqlite3.connect('test.db')

# Create a table for customer data
conn.execute('''CREATE TABLE customers1
             (ACCOUNT_NO INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             BALANCE INT NOT NULL);''')

# Insert data into the table
conn.execute("INSERT INTO customers1 (ACCOUNT_NO, NAME, BALANCE) \
              VALUES (1001, 'John', 75000)")
conn.execute("INSERT INTO customers1 (ACCOUNT_NO, NAME, BALANCE) \
              VALUES (1002, 'Jane', 90000)")
conn.execute("INSERT INTO customers1 (ACCOUNT_NO, NAME, BALANCE) \
              VALUES (1003, 'Bob', 35000)")
conn.execute("INSERT INTO customers1 (ACCOUNT_NO, NAME, BALANCE) \
              VALUES (1004, 'Alice', 55000)")

conn.commit()
# Get account number from user
account_no = input("Enter account number: ")

# Search for account details in the table
cursor = conn.execute(
    f"SELECT * FROM customers1 WHERE ACCOUNT_NO = {account_no}")
data = cursor.fetchone()

# Display the account details
if data is not None:
    print(f"Account number: {data[0]}")
    print(f"Name: {data[1]}")
    print(f"Balance: {data[2]}")
else:
    print("Account not found")


# Close the connection
conn.close()
