import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()
cursor.execute('''
    DELETE FROM clean_vocabulary
''')
connect.commit()
cursor.execute("VACUUM")
connect.commit()