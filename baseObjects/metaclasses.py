# A metaclass is a class whose instances are classes. 
# Like an "ordinary" class defines the behavior of the instances of the class, a metaclass 
# defines the behavior of classes and their instances. They inherit from the class 'type'

# When an instance of a regular class is being created; the class code is parsed into the 'type' 
# object creator function:
#   type(classname, superclasses, attributedict)
# this function will subsequentally run the functon
#   type.__new__(typeclass, classname, superclasses, attributedict)

# Metaclasses, hijack this process as we write our own object creator function, which then must
# run 'type''s __new__ method. This '__new__' method is run once for each child class that comes into play
# (which makes sense as you don't want to be making classes that aren't used)

class metaclassExample(type):

    def __new__(Class, classname, superclasses, attributedict):
        print("Running the metaclassExample __new__ method")
        print("classname: ", classname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        # other code can be written here to add methods or attributes to the object being created (which is 'Class')
        # though the following line must be run to actually create the class proper
        return type.__new__(Class, classname, superclasses, attributedict)

class regularClass1(metaclass=metaclassExample):
    value = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name 

class regularClass2(metaclass=metaclassExample):
    value = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name 

a = regularClass1("James")
b = regularClass1("Sarah") # this does not invoke the '__new__' method, as the class was already put together in the line above
c = regularClass2("Phil")
print()







# Making Singleton classes
# These are classes that are only used to make one (or a limited number of) objects of that class

# remember: the '__call__' method is run when the instance this class creates is run like a function
# in this case; that's when the class under the metaclass is run to create an instance of that class
# Unlike the '__new__' method however, it is run every time. Also the '__call__' method gets the result 
# of the '__new__' method to work with

# ..I'm not totally sure how the command "super().__call__()" works to create an instance of the child class

class Singleton(type):
    _instances = {}
    def __call__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__()
            # this line appears to somehow call the child constructor, creating an instance of 
            # the child and placing it in a location in the '_instances' list (which is stored 
            # in the metaclass) based on a hash of that child class
            # Thus, only one instance of a child class can exist
        return cls._instances[cls]

    def __new__(Class, classname, superclasses, attributedict):
        print("Running the Singleton __new__ method")
        return type.__new__(Class, classname, superclasses, attributedict)

class SingletonClass(metaclass=Singleton):
    atr = 10

x = SingletonClass()
y = SingletonClass()

print()
print(x == y)
print(x is y)
print(id(x), id(y)) # they are literally the same object
print(str(type(x)) + " at location " + hex(id(x)))

print(x.atr)
x.atr = 100
print(y.atr)
print()