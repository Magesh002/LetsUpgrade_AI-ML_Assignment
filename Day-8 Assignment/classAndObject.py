class Emp:
    """Common base class of all Emp"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Emp.empCount += 1

    def displayCount(self):
        print("Total emp is:", Emp.empCount)

    def displayEmp(self):
        print("Count id:", Emp.empCount, "Name:", self.name, "and Salary:", self.salary)


emp1 = Emp("Mag", "1000")
emp1.displayEmp()
emp2 = Emp("Test", "500")
emp2.displayEmp()

print(getattr(emp1, 'name'))
setattr(emp1, 'name', 'setMag')
emp1.displayEmp()
print(hasattr(emp1, 'age'))
print(Emp.__doc__)


class Parent:

    parentAtt = 100

    def __init__(self):
        print("Calling parent class constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAtt(self, attr):
        self.parentAtt = attr

    def getAtt(self):
        print("Parent Att is:", self.parentAtt)


class Child(Parent):

    def __init__(self):
        # super().__init__()
        print("Calling Child class constructor")

    def childMethod(self):
        print("Calling child method")


c = Child()
c.childMethod()
c.parentMethod()
c.getAtt()
c.setAtt(150)
c.getAtt()


class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector(%d, %d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a - other.a, self.b - other.b)


v1 = Vector(2, 10)
v2 = Vector(3, -2)
print(v1 + v2)