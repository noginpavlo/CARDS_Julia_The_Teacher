# from extractor import Extractor
# import sqlite3
#
# extractor = Extractor()
#
#
#     def create_database(self):
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS vocabulary
#             (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             date TEXT,
#             word TEXT,
#             phonetics TEXT,
#             definition TEXT,
#             example TEXT
#             )
#         ''')
#         self.connect.commit()
#         self.connect.close()
#
#     def save_word(self):
#         self.cursor.execute('''
#             INSERT INTO vocabulary (date, word, phonetics, definition, example)
#             VALUES (?, ?, ?, ?, ?);
#         ''', (extractor.date, extractor.word, extractor.phonetics, extractor.definition, extractor.example))
#         print("done")
#         self.connect.commit()
#         self.connect.close()