import MySQLdb
import MySQLdb.cursors

from Logger import *


class Database:
    databaseConnection = None
    databaseCursor = None

    def __init__(self):
        pass

    def connection(self, host, user, password, db):
        try:
            if password:
                self.databaseConnection = MySQLdb.connect(
                    host=host,
                    user=user,
                    passwd=password,
                    db=db,
                    cursorclass=MySQLdb.cursors.DictCursor
                )
            else:
                self.databaseConnection = MySQLdb.connect(
                    host=host,
                    user=user,
                    db=db,
                    cursorclass=MySQLdb.cursors.DictCursor
                )

            self.databaseConnection.set_character_set('utf8')

            Logger.info("Database connection succeeded.")

            self.databaseCursor = self.databaseConnection.cursor()
            self.databaseCursor.execute('SET NAMES utf8;')
            self.databaseCursor.execute('SET CHARACTER SET utf8;')
            self.databaseCursor.execute('SET character_set_connection=utf8;')

            return True

        except (MySQLdb.Error, MySQLdb.Error) as e:
            Logger.err("Database connection failed: " + str(e))
            return False

    def query(self, query):
        Logger.dbg('SQL query: "{}"'.format(query))

        try:
            self.databaseCursor.execute(query)
            result = self.databaseCursor.fetchall()

            num = 0
            for row in result:
                num += 1
                Logger.dbg('Row {}.: '.format(num) + str(row))

            return result

        except (MySQLdb.Error, MySQLdb.Error) as e:
            Logger.err(e)

            return False

    def insert(self, query):
        Logger.dbg('SQL query: "{}"'.format(query))

        try:
            res = self.databaseCursor.execute(query)

            # Commit new records to the database
            result = self.databaseConnection.commit()
            return res

        except (MySQLdb.Error, MySQLdb.Error) as e:
            Logger.err(e)

            # Rollback introduced changes
            self.databaseConnection.rollback()
            return 0

    def delete(self, query):
        return self.insert(query)