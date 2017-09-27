#   An abstract class, is a class that contains one or more abstract methods, 
# which are methods that are declared but contain no implementation
#   To create an abstract class, we must import the 'abc' module (Abstract 
# Base Classes) as we inherit an object from there into the abstract class we make

import abc

class abstractClass(abc.ABC):
    def __init__(self, value):
        self.value = value
    
    @abc.abstractmethod
    def do_something(self):
        pass

# any class that inherits this class but does not implement the abstract methods,
# is itself an abstract class (implementation is simply overriding)

class antherAbstractClass(abstractClass):
    pass

class fullClass(antherAbstractClass):
    def do_something(self):
        return self.value + 42

x = fullClass(10)
print( x.do_something() )
print()



#   In addition, one is able to put code into the abstract method. Though derived classes
# must override this abstract method; it is still possible to run the method from the 
# overriding method

class abstractClass_withMethodCode(abc.ABC):
    def __init__(self, value):
        self.value = value
    
    @abc.abstractmethod
    def do_something(self):
        print("welcome to the abstract do_something method")

class fullClas_withMethodCodes(abstractClass_withMethodCode):
    def do_something(self):
        print("welcome to the full do_something method")
        super().do_something()
        return self.value + 42

x = fullClas_withMethodCodes(10)
print( x.do_something() )
print()