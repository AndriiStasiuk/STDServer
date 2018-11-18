import sqlite3

#Open database
conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE power
    (
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     powerValue DOUBLE,
     eventTime DATETIME
    )''')

conn.execute('''CREATE TABLE angel
    (
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     angelValue DOUBLE,
     eventTime DATETIME
    )''')