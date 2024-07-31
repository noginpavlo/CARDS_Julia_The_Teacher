from datetime import date
import requests
import random
import json


class Extractor:

    def __init__(self, word):
        self.word = word
        self.url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{self.word}'
        self.date = str(date.today())
        self.response = {}
        self.definition = []
        self.example = []
        self.json = {}


    def get_definition(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.response = response.json()
            try:
                word = self.word.upper()
                record_date = self.date
                phonetics = self.response[0]['phonetic']
                example = self.response[0]['meanings'][0]['definitions'][0]['example']
                definition = self.response[0]['meanings'][0]['definitions'][0]['definition']
                return record_date, word, phonetics, definition, example
            except KeyError:
                word = self.word.upper()
                record_date = self.date
                phonetics = self.response[0]['phonetic']
                definition = self.response[0]['meanings'][0]['definitions'][0]['definition']
                example = "No example found."
                return record_date, word, phonetics, definition, example
        else:
            return f"Unable to find definition for '{self.word}"

    def format(self):
        record_date = self.date
        word = self.json["key_word"]
        phonetics = self.response[0]['phonetic']
        definition = self.definition
        example = self.json["example"]
        return record_date, word, phonetics, definition, example


    # def store_data(self, json_dict):
    #     with open("database.json", "r") as file:
    #         entry_store = json.load(file)

        # entry_store.append(json_dict)
        #
        # with open("database.json", "w") as file:
        #     json.dump(entry_store, file, indent=4, sort_keys=False)

    # def retrieve(self):
    #     with open("database.json", "r") as file:
    #         data = json.load(file)
    #         database_length = len(data)
    #         index = random.randint(0, database_length-1)
    #         word_to_learn = data[index]
    #         return word_to_learn
    #
    # def get_back(self, json_word):
    #     title_word = json_word["key_word"]
    #     prompt = json_word["prompt"]
    #     phonetics = json_word["phonetics"]
    #     definition = json_word["definitions"]
    #     example = json_word["example"]
    #     final_text = f"{title_word}\n{prompt}\n{definition}\n{phonetics}\nExample: {example}"
    #     print(final_text)
    #
    # def get_front(self, json_word):
    #     pass
