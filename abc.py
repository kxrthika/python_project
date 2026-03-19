from abc import ABC, abstractmethod

class absclass (ABC):
    def print(self, x):
        print ("passed value", x)
    @abstractmethod
    def task(self):
        print("we are inside absclass task")
class text_class(absclass):
    def task(self):
        print("we are inside text_class task")
test_obj = text_class()
test_obj.task()
test_obj.print(20)
