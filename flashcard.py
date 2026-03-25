class flashcard:
    def __init__ (self, word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word +'('+self.meaning+')'
flash = []
print ("welcome to flash card appilation")
while(True):
    word = input("enter the name u want to add on the flash card")
    meaning = input("enter the meaning of the word")
    flash.append(flashcard(word,meaning))
    option = int(input("enter 0 , if u want to add another word otherwise aenter 1"))
    if (option):
        break 
print("\nyour flashcards")
for i in flash:
    print(">",i)


    