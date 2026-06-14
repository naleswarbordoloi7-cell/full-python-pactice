# # it allows code reuse
class Animal:
    def sound(self):
        print("animals makes sounds")

class dog(Animal):
    def bark(self):
        print("dog barks")

dog = dog()
dog.sound()
dog.bark()


# using super() funtion
class Person:
    def __init__(self,name):
        self.name=name

class student(Person):
    def __init__(self, name,rool):
        super().__init__(name)
        self.rool =rool

    def display(self):
        print("name:",self.name)
        print("rool:",self.rool)

s = student("naleswar",6)
s.display()