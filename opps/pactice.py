class Myclass  :
    className = "Myclass"
    def sayhello(self,name):
        print(f"hello,{name}!, i am a {self.className}.")
obj = Myclass()
obj.sayhello("naleswar")
 

class calculator:
    def add(self,x,y):

      return x + y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        return x/y
    


class student:
    def __init__(self,name,adnumber):
        self.name = name
        self.adnumber = adnumber
        