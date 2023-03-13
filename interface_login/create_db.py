import sqlite3

# connection
connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

# queries
# create the database in a table called users that contains name, password and email
command = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT, email TEXT)"""
# execute the command
cursor.execute(command)

# Add new column to users table
alter_command = """ALTER TABLE users ADD COLUMN email TEXT;"""
cursor.execute(alter_command)

# Insert users into the table
cursor.execute("INSERT INTO users VALUES('imen','123','imen@gmail.com')")
cursor.execute("INSERT INTO users VALUES('ouma','1234','ouma@gmail.com')")
cursor.execute("INSERT INTO users VALUES('tasnim','1235','tasnim@gmail.com')")

# commit the changes
connection.commit()
