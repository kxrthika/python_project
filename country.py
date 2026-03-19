class India():
    def capital(self):
        print("New delhi is the capital of india")
    def  language(self):
        print("Hindi is the language most widely used")
    def type(self):
        print("inida is a develping country")
class USA():
    def capital(self):
        print("DC is the capital of USA")
    def  language(self):
        print("English is the language most widely used")
    def type(self):
        print("USA is a developed country")
obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()