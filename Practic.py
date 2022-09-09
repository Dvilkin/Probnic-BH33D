import sqlite3


conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(20) UNIQUE NOT NULL
);
''')
