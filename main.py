from extractor import Extractor
from windows import Window

menu = Window()
menu.mainloop()

definition = Extractor("love")
new_entry = definition.get_definition()
definition.store_data(new_entry)
temorary_var = definition.retrieve()
definition.get_back(temorary_var)

