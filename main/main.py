import sqlite3

sqliteConnection = None


def init(): # create both
    global sqliteConnection
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    create_tables(cursor)


def create_tables(cursor):
    query = ""  # todo read from table_creator file
    cursor.execute(query)
    cursor.close()
    pass


def get_command(command):
    pass


in_ = input()
get_command(in_)