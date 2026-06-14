# many forms/actions depending on the object
class Shape:
    def area(self):
        print("calculating area")
class circle(Shape):
    def area(self):
        print("area of circle")
class rectangle(Shape):
    def area(self):
        print("area of rectangle")

c = circle()
r = rectangle()
c.area()
r.area()


class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")
obj =A()
obj =B()
obj.show()