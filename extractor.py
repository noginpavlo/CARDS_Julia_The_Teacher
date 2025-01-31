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
        connect.commit()
        connect.close()
        if result[0] > 0:
            return "Word already in dictionary"
        elif response.status_code == 200:
            self.response = response.json()
            word = input_word.upper()
            record_date = self.date
            try:
                phonetics = self.response[0]['phonetic']
            except KeyError:
                phonetics = "not found"
            definition = self.response[0]['meanings'][0]['definitions'][0]['definition']
            try:
                example = self.response[0]['meanings'][0]['definitions'][0]['example']
            except KeyError:
                example = "No example found."
            increment = 1
            return record_date, word, phonetics, definition, example, increment
        else:
            return "Unable to find"

    def save_word(self, array):
        if len(array) == 6:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute('''
                   INSERT INTO vocabulary (date, word, phonetics, definition, example, increment)
                   VALUES (?, ?, ?, ?, ?, ?);
               ''', (array[0], array[1], array[2], array[3], array[4], array[5]))
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
            example TEXT,
            increment INT
            )
        ''')
        connect.commit()
        connect.close()

    def create_clean_data_table(self):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS words_for_today
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
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute('''
                SELECT MAX(id) FROM vocabulary
            ''')
            result = cursor.fetchone()
            max_id = result[0]
        random_word_id = 1
        if max_id >= 1:
            random_word_id = random.randint(1, max_id)
        return random_word_id

    def make_card(self, card_id):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute('''
                SELECT * FROM vocabulary WHERE id = ? AND date <= ?
                    ''', (card_id, date.today()))
            row = cursor.fetchall()

            word_title = row[0][2]
            word_phonetics = row[0][3]
            word_definition = row[0][4]
            word_example = row[0][5]

        def create_front(word):
            word = word.capitalize()
            print(word)
            return word

        def create_back(title, phonetics, definition, example):
            compose_string = ""
            compose_string += f"{title.upper()}"
            if phonetics == "not found":
                pass
            else:
                compose_string += f"\nPhonetics: {phonetics}"
            compose_string += f"\nDefinition: {definition}"
            if example == "No example found.":
                pass
            else:
                compose_string += f"\nExample: {example}"
            print(compose_string)
            return compose_string

        front = create_front(word_title)
        back = create_back(word_title, word_phonetics, word_definition, word_example)

        return front, back
