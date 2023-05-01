import sqlite3

# Create a database connection
conn = sqlite3.connect('test.db')


cursor = conn.execute("SELECT * FROM customers1 WHERE BALANCE > 50000")
data = cursor.fetchall()

# Display the customer details
if data:
    print("Customers with balance > Rs. 50000/-:")
    for row in data:
        print(f"Account number: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Balance: {row[2]}")
        print("---------------")
else:
    print("No customers with balance > Rs. 50000/- found")

# Close the connection
conn.close()
