"""
class ClassName:
    'Optional class documentation string': ClassNAme.__doc__
    class_suite: all the component statements
"""

# e.g.
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)

e1 = Employee("John Dobson", 140000)
e1.displayCount()
e1.displayEmployee()

"""
    getattr(e1, 'salary') # Returns the value of 'salary' att
    setattr(e1, 'salary', 400000) # Sets the value of 'salary' att w/ input value
    delattr(e1, 'salary')
    hasattr(e1, 'salary') # Returns true if 'salary' att exists
"""

"""
    Built-in class attributes
    __dict__: dictionary containing the class's namespace
    __doc__: class documentation string or none
    __name__: class name
    __module__: module name in which the class is define. This att is "__main__" in interactive mode
    __basses__: a possibly empty tuple containing the base classes, in the order of their occurrence in the base class list

"""

# Garbage collection
a = 40  # Object created
b = a   # Ref count +=1
c = [b] # Ref count +=1

del a   # Ref count -=1
b = 100 # Ref count -=1
c[0] = -1 # Ref count -=1

# __del__() destructor
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1

print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3
# Can note here that the id for all three objects is the same

"""
    Creating a subclass of an already existing class(es)
    class SubClassName (ParentClass1 [, ParentClass2, ...]):
        'optional class documentation string'
        class_suite
"""

class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")
    
    def parentMethod(self):
        print ('Calling parent method')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print ("Parent attribute:", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print ("Calling child constructor")
    
    def childMethod(self):
        print ("Calling child method")

"""
    issubclass(sub, sup)
    isinstance(obj, Class)
"""

# Overriding methods
"""
class Parent: 
    def myMethod(self):
        print('Calling parent method')

class Child(Parent):
    def myMethod(self):
        print('Calling child method')
"""

# Base Overloading Methods
"""
    __init__ (self [,args]): constructor
    __del__(self): destructor
    __repr__(self): evaluatable string representation
    __str__(self): printable string representation
    __cmp__(self, x): object comparison
"""

# e.g.
class Vector:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    
    def __str__ (self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__ (self, other):
        return Vector (self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5, -2)
print( v1 + v2) # uses __str__ method

# Data hiding: __[secret variable name]
class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print(counter.__secretCount)
## Can access hidden att as object._classNAme__attrNAme
print(counter._JustCounter__secretCount)