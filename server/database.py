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

conn.execute('''CREATE TABLE humidity
    (
  id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  humidityValue DOUBLE,
  eventTime     DATETIME 
    )''')

conn.execute('''CREATE TABLE rain
(
  id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  eventTime DATETIME,
  action    INTEGER
 )''')

conn.execute('''CREATE TABLE stream
(
  id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  streamValue DOUBLE,
  eventTime   DATETIME 
 )''')

conn.execute('''CREATE TABLE voltage
(
  id           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  voltageValue DOUBLE,
  eventTime    DATETIME
 )''')