# from datetime import datetime, timedelta
#
# time = "2024-01-01"
# time_format = "%Y-%m-%d"
# new_time = datetime.strptime(time, time_format)
# increment = 10
# add_days = timedelta(days=increment)
# time = new_time.date() + add_days
# print(time)
# import sqlite3
#
# date = "2025-12-12"
# word = "NOGO"
# phon = "NOGO"
# defin = "NOGO"
# exa = "NOGO"
# increment = 1
#
# connect = sqlite3.connect("database.db")
# cursor = connect.cursor()
# cursor.execute('''
#            INSERT INTO vocabulary (date, word, phonetics, definition, example, increment)
#                    VALUES (?, ?, ?, ?, ?, ?);
#                ''', (date, word, phon, defin, exa, increment))
#
# connect.commit()
# connect.close()

import random

print(random.randint(1, 1))
