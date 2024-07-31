import sqlite3

connect = sqlite3.connect("database.db")

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vocabulary 
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    phonetics TEXT,
    definition TEXT,
    example TEXT
    )
''')


