from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    def display(self):
        print("This is abstract class")

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Record inserted into SQL Database")
    def update(self):
        print("SQL Database updated")
    def delete(self):
        print("Record deleted from SQL Database")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Record inserted  into No SQL Database")
    def update(self):
        print("No SQL Database updated")
    def delete(self):
        print("Record deleted from No SQL Database")

sql_obj = SQLDatabase()
sql_obj.insert()
sql_obj.update()
sql_obj.delete()

no_sql_obj = NoSQLDatabase()
no_sql_obj.insert()
no_sql_obj.update()
no_sql_obj.delete()