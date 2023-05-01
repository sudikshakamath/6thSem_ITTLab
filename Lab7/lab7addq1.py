import sqlite3
import re

# connect to the database
conn = sqlite3.connect('test.db')

# create a cursor object
cursor = conn.cursor()

# create the customers table if it doesn't exist
cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)')

# add some sample customer data to the table
customers = [
    ('John Doe', '5555551234', 'johndoe@example.com'),
    ('Jane Smith', '5555555678', 'janesmith@example.com'),
    ('Bob Johnson', '5555559012', 'bobjohnson@example.com'),
    ('Mary Brown', '5555553456', 'marybrown@example.com'),
    ('Tom Davis', '5555557890', 'tomdavis@example.com'),
]
cursor.executemany(
    'INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)', customers)

# prompt the user to enter a phone number and email address
phone = input('Enter a phone number to validate: ')
email = input('Enter an email address to validate: ')

# query the database for customer data
cursor.execute('SELECT name, phone, email FROM customers')

# iterate over the results and check if any phone numbers or email addresses match the user's input
matches = []
for row in cursor.fetchall():
    name, db_phone, db_email = row
    if db_phone == phone and db_email == email:
        matches.append(
            f'{name} has phone number {phone} and email address {email}')

# print the results
if matches:
    print('The following customers have matching phone numbers or email addresses:')
    for match in matches:
        print(match)
else:
    print('No customers have matching phone numbers or email addresses.')

conn.close()
