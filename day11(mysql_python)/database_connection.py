# Python implementation to create a Database in MySQL
import pymysql
# connecting to the mysql server
db = pymysql.connect(
	host="localhost",
	user="root",
	passwd="Arun@0005",
    database = "department_db"
)

# cursor object c
c = db.cursor()

# executing the create database statement
# c.execute("CREATE DATABASE department_db")

# fetching all the databases
# c.execute("SHOW DATABASES")
# c.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]


# c.execute("SELECT * from customers")
# # c.execute("SELECT name, address from customers")
# myresult = c.fetchone()

# for x in myresult:
#   print(x)
# db.commit()

# print(c.rowcount, "record inserted.")

# printing all the databases
# for i in c:
# 	print(i)
# c = db.cursor()

# finally closing the database connection
# db.close()