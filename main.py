from windows import Window
from extractor import Extractor


extractor = Extractor()

menu = Window()
menu.mainloop()

print(extractor.make_card(extractor.pull_random_card()))





