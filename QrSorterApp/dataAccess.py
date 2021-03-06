import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.dbFile = '/home/pi/Desktop/Database.db'
        self.createTable()

    def createConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.dbFile)
        except Error as e:
            print(e)
        
        return connection

    def createTable(self):
        sql = '''create table if not exists Categories(
                id integer primary key,
                categoryName text not null,
                numberOfProducts integer not null,
                boxId integer not null,                
                unique(categoryName)
            );'''
        connection = self.createConnection()
        
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def addCategory(self, category, numberOfProducts, boxId):
        sql = '''insert into Categories(categoryName, numberOfProducts, boxId)
            values(?, ?, ?)'''
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql, (category, numberOfProducts, boxId))
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def getCategories(self):
        sql = 'select * from Categories'
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

        return rows

    def getBoxByCategory(self, category):
        sql = 'select boxId from Categories where categoryName = ?'
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql, (category, ))
            row = cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

        return row[0]

    def updateCategory(self, id, category, numberOfProducts, boxId):
        sql = '''update Categories
                set categoryName = ?,
                    numberOfProducts = ?,
                    boxId = ?
                where id = ?'''
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql, (category, numberOfProducts, boxId, id))
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def deleteCategory(self, id):
        sql = 'delete from Categories where id = ?'
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def deleteAll(self):
        sql = 'delete from Categories'
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def resetCategoriesCounters(self):
        categories = self.getCategories()
        for c in categories:
            self.updateCategory(c[0], c[1], 0, c[3])

if __name__ == '__main__':
    db = Database()

    categories = db.getCategories()
    for c in categories:
        print(c)
