import pymysql

def connect_db():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Arun@0005',
            database='department_db',
            cursorclass=pymysql.cursors.DictCursor
        )
        print('MySQL connected successfully')
        return connection
    except pymysql.MySQLError as err:
        print(f"Something went wrong: {err}")
        return None

def create_table(connection):
    with connection.cursor() as cursor:
        try:
            query = """CREATE TABLE EMPLOYEE (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255),
                        age INT,
                        salary INT
                    );"""
            cursor.execute(query)
            connection.commit()
            print('Table created successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def inserting_data(connection):
    with connection.cursor() as cursor:
        try:
            query = "INSERT INTO EMPLOYEE(name, age, salary) VALUES (%s, %s, %s)"
            n = int(input("Enter the number of records to be inserted: "))
            data = []
            for i in range(n):
                name = input(f"Enter the name of employee {i + 1}: ")
                age = int(input(f"Enter the age of employee {i + 1}: "))
                salary = int(input(f"Enter the salary of employee {i + 1}: "))
                data.append((name, age, salary))
            cursor.executemany(query, data)
            connection.commit()
            print('Data inserted successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def select_all_data(connection):
    with connection.cursor() as cursor:
        try:
            query = "SELECT * FROM EMPLOYEE;"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as err:
            print(f'Something went wrong: {err}')

def updating_data(connection):
    with connection.cursor() as cursor:
        try:
            query = "UPDATE EMPLOYEE SET salary = 7000 WHERE name = 'shanmuk';"
            cursor.execute(query)
            connection.commit()
            print('Updated the data successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def deleting_data(connection):
    with connection.cursor() as cursor:
        try:
            query = "DELETE FROM EMPLOYEE WHERE id = 1;"
            cursor.execute(query)
            connection.commit()
            print('Data deleted successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def sort_data(connection):
    with connection.cursor() as cursor:
        try:
            query = "SELECT * FROM EMPLOYEE ORDER BY salary DESC;"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as err:
            print(f'Something went wrong: {err}')

def query_with_filter(connection):
    with connection.cursor() as cursor:
        try:
            query = "SELECT * FROM EMPLOYEE WHERE salary > %s;"
            cursor.execute(query, (5000,))
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as err:
            print(f'Something went wrong: {err}')

def drop_table(connection):
    with connection.cursor() as cursor:
        try:
            query = "DROP TABLE EMPLOYEE;"
            cursor.execute(query)
            connection.commit()
            print('Table dropped successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def drop_database(connection):
    with connection.cursor() as cursor:
        try:
            query = "DROP DATABASE department;"
            cursor.execute(query)
            connection.commit()
            print('Database dropped successfully')
        except pymysql.MySQLError as err:
            print(f"Something went wrong: {err}")

def main():
    connection = connect_db()
    if not connection:
        return None
    create_table(connection)
    inserting_data(connection)
    # updating_data(connection)
    # deleting_data(connection)
    # sort_data(connection)
    query_with_filter(connection)
    # drop_table(connection)
    # select_all_data(connection)
    # drop_database(connection)
    connection.close()
    print('MySQL connection closed')

main()
