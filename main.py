from windows import Window
from extractor import Extractor


extractor = Extractor()

menu = Window()
menu.mainloop()

card_number = extractor.pull_random_card()
extractor.make_card(card_number)




