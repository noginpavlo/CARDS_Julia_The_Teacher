from datetime import date
import requests
import random
import sqlite3


class Extractor:

    def __init__(self):
        self.date = str(date.today())
        self.response = {}
        self.definition = []
        self.example = []
        self.json = {}
        self.storage = self.get_definition


    def get_definition(self, input_word):
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{input_word}'
        response = requests.get(url)
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        # lower_input_word =
        cursor.execute('''
            SELECT COUNT (*) FROM vocabulary WHERE word = ?
        ''', (input_word.upper(), ))
        result = cursor.fetchone()
        print(result)
        print(result[0])
        connect.commit()
        connect.close()
        if result[0] > 0:
            return "Word already in dictionary"
        elif response.status_code == 200:
            self.response = response.json()
            word = input_word.upper()
            record_date = self.date
            phonetics = self.response[0]['phonetic']
            definition = self.response[0]['meanings'][0]['definitions'][0]['definition']
            try:
                example = self.response[0]['meanings'][0]['definitions'][0]['example']
                return record_date, word, phonetics, definition, example
            except KeyError:
                example = "No example found."
                return record_date, word, phonetics, definition, example
        else:
            return "Unable to find"

    def save_word(self, array):
        if len(array) == 5:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute('''
                   INSERT INTO vocabulary (date, word, phonetics, definition, example)
                   VALUES (?, ?, ?, ?, ?);
               ''', (array[0], array[1], array[2], array[3], array[4]))
            print("successfully saved")
            connection.commit()
            connection.close()
        else:
            print(array)

    def create_database(self):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vocabulary
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            word TEXT,
            phonetics TEXT,
            definition TEXT,
            example TEXT
            )
        ''')
        connect.commit()
        connect.close()

    def create_clean_data_table(self):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clean_vocabulary
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            word TEXT,
            phonetics TEXT,
            definition TEXT,
            example TEXT
            )
        ''')
        connect.commit()
        connect.close()

    def pull_random_card(self):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute('''
            SELECT MAX(id) FROM vocabulary
        ''')
        result = cursor.fetchone()
        max_id = result[0]
        random_word_id = random.randint(1, max_id)
        connect.close()
        print(random_word_id)
        return random_word_id

    def make_card(self, card_id):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute('''
            SELECT * FROM vocabulary WHERE id = ?
                ''', (card_id, ))
        row = cursor.fetchall()
        word_id = row[0][0]
        word_date = row[0][1]
        word_title = row[0][2]
        word_phonetics = row[0][3]
        word_definition = row[0][4]
        word_example = row[0][5]
        print(word_id, word_date, word_title, word_phonetics, word_definition, word_example)


