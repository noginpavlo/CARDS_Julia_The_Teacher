from extractor import Extractor
from tkinter import *
import random


extractor = Extractor()


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Julia The Teacher")
        self.geometry("300x400")
        self.card_flip_side = 1
        self.current_curd = ""

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

        self.input = StringVar()

    def run_learn(self):
        learn_window = Toplevel(self)
        learn_window.title("Learn with Julia")
        learn_window.minsize(380, 400)

        learn_frame = Frame(learn_window)
        learn_frame.grid(sticky="news")

        canvas = Canvas(learn_frame, bg="white")
        canvas.grid(row=0, column=0, sticky="news")

        text_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=text_frame, anchor="nw")

        text_label = Label(text_frame, text="Press 'Flip' to tart learning.", font=("Arial", 16),
                           bg="white", fg="black", wraplength=380)
        text_label.pack()

        def show_card():
            if self.card_flip_side == 1:
                self.current_card = extractor.make_card(extractor.pull_random_card())
                text_label.config(text=self.current_card[0])
                self.card_flip_side = 2
            elif self.card_flip_side == 2:
                text_label.config(text=self.current_card[1])
                self.card_flip_side = 1

        flip_button = Button(learn_frame, text="Flip", font=("Arial", 24), command=show_card,)
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
        create_frame.grid(sticky="news", padx=10, pady=10)

        create_frame.grid_rowconfigure(0, weight=1)
        create_frame.grid_rowconfigure(1, weight=1)
        create_frame.grid_rowconfigure(2, weight=1)
        create_frame.grid_columnconfigure(0, weight=1)
        create_frame.grid_columnconfigure(1, weight=1)
        create_frame.grid_columnconfigure(2, weight=1)

        self.input_entry = Entry(create_frame, textvariable=self.input, font=("Arial", 14))
        self.input_entry.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

        def create_placeholder():
            self.input_entry.insert(0, "Type your word here...")
            self.input_entry.config(fg="grey")

        def remove_placeholder(_):
            if self.input_entry.get() == "Type your word here...":
                self.input_entry.delete(0, END)
                self.input_entry.config(fg="black")

        def add_placeholder(_):
            if not self.input_entry.get():
                self.input_entry.insert(0, "Type your word here...")
                self.input_entry.config(fg="grey")

        create_placeholder()
        self.input_entry.bind("<FocusIn>", remove_placeholder)
        self.input_entry.bind("<FocusOut>", add_placeholder)

        self.create_button = Button(create_frame, text="Create card", command=self.refresh_prompt, font=("Arial", 24))
        self.create_button.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

        self.done_widget = Text(create_frame, state=DISABLED,  width=30, height=2, wrap='word', font=("Arial", 14))
        self.done_widget.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        card_window.grid_rowconfigure(0, weight=1)
        card_window.grid_columnconfigure(0, weight=1)

    def refresh_prompt(self):
        input_word = self.input.get()
        word = extractor.get_definition(input_word)
        if word == "Unable to find":
            self.done_widget.config(state=NORMAL)
            self.done_widget.delete("1.0", END)
            self.done_widget.insert(END,  f"Unable to find '{input_word}'")
            self.done_widget.config(state=DISABLED)
        elif word == "Word already in dictionary":
            self.done_widget.config(state=NORMAL)
            self.done_widget.delete("1.0", END)
            self.done_widget.insert(END, f"Word '{input_word}' already in your dictionary")
            self.done_widget.config(state=DISABLED)
        else:
            extractor.save_word(word)

            self.done_widget.config(state=NORMAL)
            self.done_widget.delete("1.0", END)
            self.done_widget.insert(END, f"'{input_word}' added successfully")
            self.done_widget.config(state=DISABLED)


    def run_stats(self):
        pass

    def run_settings(self):
        pass
