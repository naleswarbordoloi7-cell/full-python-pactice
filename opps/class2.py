# create a car class
class Car :
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def display(self):
        print("brand:",self.brand)
        print("color:",self.color)

# 1 pactics
car1 = Car("toyota","red")

car1 .display()


class Person:
    def __init__(self,name):
        self.name = name

p =Person("ram")
print(p.name)

# 2 pactics
class Dog:
    def bark(self):
        print("woof!")
d = Dog()
d.bark()

# Book class
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author =author

book1 = Book("Python Programming","Guido van Rossum")

print("title:",book1.title)
print("author:",book1.author)