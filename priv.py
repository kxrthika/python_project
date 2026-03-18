class myclass:
    __privateVar = 27;
    def __privMeth(self):
        print("I'm inside my class")
    def hello(self):
        print("private variable values", myclass.__privateVar)

foo = myclass()
foo.hello()
foo.__privMeth()