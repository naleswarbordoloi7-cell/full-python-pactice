# show what an object does, hide how it does .
from abc import ABC,  abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):

    def sound(self):
        print("dog barks")

dog = dog()
dog.sound()



# Payment system

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class creditcard(payment):

    def pay(self,amount):
        print(f"paid ${amount} using credit card")

class UPI(payment):
    def pay(self,amount):
        print(f"paid ${amount} using UPI")

p1 =creditcard()
p1.pay(100)

p2 = UPI()
p2.pay(200)
