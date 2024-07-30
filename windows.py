from extractor import Extractor
from tkinter import *
import random


extractor = Extractor("word")


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Julia The Teacher")
        self.geometry("300x400")

        self.menu_frame = Frame()

        self.learn_button = Button(self.menu_frame, text="Learn", command=self.run_learn, font=("Arial", 24))
        self.learn_button.grid(row=1, column=1, columnspan=2, pady=10, sticky="news")

        self.cards_button = Button(self.menu_frame, text="Create cards", command=self.run_cards, font=("Arial", 24))
        self.cards_button.grid(row=2, column=1, columnspan=2, pady=10, sticky="news")

        self.stats_button = Button(self.menu_frame, text="Stats", command=self.run_stats, font=("Arial", 24))
        self.stats_button.grid(row=3, column=1, columnspan=2, pady=10, sticky="news")

        self.settings_button = Button(self.menu_frame, text="Settings", command=self.run_settings, font=("Arial", 24))
        self.settings_button.grid(row=4, column=1, columnspan=2, pady=10, sticky="news")

        self.menu_frame.pack()

    def run_learn(self):
        learn_window = Toplevel(self)
        learn_window.title("Learn with Julia")
        learn_window.minsize(300, 400)

        learn_frame = Frame(learn_window)

        text_widget = Text(learn_frame, wrap="word", font=("Arial", 14))
        text_widget.insert("1.0", "This is some text to display in the window. " * 10)
        text_widget.config(state="disabled")  # Make the text widget read-only
        text_widget.grid()

        flip_button = Button(learn_frame, text="Flip", font=("Arial", 24))
        flip_button.grid(row=1, column=0, pady=5, sticky="news")

        easy_button = Button(learn_frame, text="Easy", bg="lightgreen", font=("Arial", 24))
        easy_button.grid(row=2, column=0, pady=5, sticky="news")

        medium_button = Button(learn_frame, text="Medium", bg="lightyellow", font=("Arial", 24))
        medium_button.grid(row=3, column=0, pady=5, sticky="news")

        hard_button = Button(learn_frame, text="Hard", bg="lightpink", font=("Arial", 24))
        hard_button.grid(row=4, column=0, pady=5, sticky="news")

        learn_frame.grid()

    def run_cards(self):
        card_window = Toplevel(self)
        card_window.title("Create cards")
        card_window.minsize(600, 400)

        create_frame = Frame(card_window)
        create_frame.grid(sticky="news")

        card_window.grid_rowconfigure(0, weight=1)
        card_window.grid_columnconfigure(0, weight=1)

        create_frame.grid_rowconfigure(0, weight=1)
        create_frame.columnconfigure(0, weight=1)
        create_frame.columnconfigure(1, weight=1)
        create_frame.columnconfigure(2, weight=1)

        input_var = StringVar()
        input_entry = Entry(create_frame, textvariable=input_var, font=("Arial", 14))
        input_entry.grid(row=0, column=1, pady=5, sticky="ew")

        create_button = Button(create_frame, text="Create card", command=extractor.get_definition, font=("Arial", 24))
        create_button.grid(row=1, column=1, pady=5, sticky="ew")


    def run_stats(self):
        pass

    def run_settings(self):
        pass
