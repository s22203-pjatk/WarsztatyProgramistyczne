import sqlite3
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",('first title', 'first content'))

connection.commit()
connection.close()