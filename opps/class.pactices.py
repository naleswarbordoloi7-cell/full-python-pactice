# Employee class
class employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary =salary

emp1 = employee('Naleswar',150000)
emp2 = employee("Anuj", 200000)

print("employee 1")
print("name:",emp1.name)
print("salary:",emp1.salary)

print("\nemployee 2")
print("name:",emp2.name)
print("salary:",emp2.salary)


# Rectangular class
class Rectangle:
    def __init__(self,lenth,width):
        self.lenth =lenth
        self.width =width
    def area(self):
        return self.lenth * self.width
rect = Rectangle(10,4)
print("area =",rect.area())