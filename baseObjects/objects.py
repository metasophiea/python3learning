# Simplist possible class
class SimplistClass:
    pass

x = SimplistClass()
print( type(x) )








# -> Attributes
# - system attributes
# these are attributes that come with any class, without the need for implementation
#   - __dict__
# objects store their attributes in a dictionary, this command displays said dictionary
print( x.__dict__ )
print()

# - the usual way
# the following is an example of defining attributes on a class level. To define attributes on an object level they must be
# declared within a method (most probably the __init__) using the self keyword as a prefix. One can define class level
# attributes within a method be using the class name as a prefix (or type(self), which is apparently a better choice) In all
# cases, the underscoring thing remains
class classWithAttributes:
    #class level attributes
    a = 10 
    b = "Hello" 
    _protectedAttribute = "dangerous stuff" # this is more of a naming convention than anything technical
    __privateAttribute = "private stuff"

    #object level attributes
    def __init__(self):
        self.c = 100

a = classWithAttributes()
print(a.a)
print(a.b)
print(a._protectedAttribute) 
# print(a.__privateAttribute) # this will return an error. Obviously; methods of this class can access this attribute freely
print()

# - dynamic attributes
# dynamically assigned attributes are attributes that you add to an object after it has been created. These are always at object level
a = SimplistClass()
b = SimplistClass()
a.name = "James" # "object level attribute"
b.name = "Conor"
print(a.name) 
print(b.name)
# simple. Notice the object's attribute list
print(a.__dict__)
print(b.__dict__)
print()
# things can become a little more complicated when you assign attributes to the class itself
SimplistClass.name = "Sarah" # "class level attribute"
# now, any object produced with this class will access the attribute 'name' from the class.
# Thus, one can change the classes attribute, effecting the results of accessing that objects
# apparent attributes
c = SimplistClass()
print(c.name)
SimplistClass.name = "Rachel"
print(c.name)
# one can see that the object does not have the attribute itself but the class does
print(c.__dict__)
print(SimplistClass.__dict__)
print()
# setting a classes attribute like this can be used for static variables of C and C++
# manually setting the object's attribute will stop the access to the class, creating 
# local attribute data
c.name = "Hannah"
print(c.name)
print(c.__dict__)
print()

# slots
# Understandably, having all objects being capable of expanding their attribute list can be costly to memory 
# efficiency. Attributes are usually stored in a dynamic dictionary, but we can force them to be stored in a 
# static dictionary with the __slots__ attribute.
class classWithSlots:
    __slots__ = ['a','b']

    def __init__(self):
        self.a = 100
        self.b = 200
        # self.c = 300      # attempting to decalare an additional object-level attribute is not allowed
# only attributes whose names were declared in that  '__slots__' list will be allowed in this object (excluding class-level attributes)
a = classWithSlots()
print(a.a)
print(a.b)
a.a = "string"          # the data stored is itself dynamic
print(a.a)
# a.c = "new Value"     # attempting to decalare an additional object-level attribute dynamically is not allowed
print()
# Apparently this inefficiency was dealt with in python3.3 with Key-Sharing Dictionaries which allow instances to share 
# part of their internal storage between one another. I'm gussing this is a clever use of pointers behind the scenes.








# -> Methods
# it's important to note that there is no overloading in python, beyond sudo overloading described later
# obviously, not having types takes away a lot of the need for overloading. Also all methods are public.
# Privacy is simulated by writing a weird mathod name (eg. "__method") the idea is that we're all supposed
# to be friends here, so go ahead and look at the interesting "private" methods; but don't use them for real

# - the usual way
class classWithMethod:
    atr = 10

    def method(self):
        print("welcome to the method - " + str(self.atr) )

x = classWithMethod()
# there are three different ways to call this method, in varing levels of weirdness
x.method()
classWithMethod.method(x)
type(x).method(x)
print()
# note; the first argument of a method will be a reference to the object instance. It doesn't have
# to be the word 'self' though this is the convention. This argument must be included however. If 
# it isn't; the method is only accessable through the class (eg. class.method() works, obj.method() 
# fails) It is possible to convert this method into a full static method:
# - dynamic method
class classWithDynamicMethod:
    atr = 34

def someFunc1():
    return 100
def someFunc2(self):
    return self.atr

a = classWithDynamicMethod()

# # -- class level addition
# classWithDynamicMethod.dynamicMethod = someFunc2         # I know, right? so long as the method is in the class before it's first called, everything is fine
# print( a.dynamicMethod() )

# # -- object level addition
# # --- easy way without self
# a.dynamicMethod1 = someFunc1
# # --- difficult way with self (needs module)
# import types
# a.dynamicMethod2 = types.MethodType( someFunc2, a )
# print( a.dynamicMethod1() )
# print( a.dynamicMethod2() )

print()

# - static method
# static methods are methods on the class level. They are unable to access non-static attributes and methods.
# They also do not pay attention to inheritance, thus these methods will access the data stored only in their
# classes static attributes; even if those attributes are redefined in a derived class 
class classWithStaticMethod:
    atr = 34

    @staticmethod
    def method():
        print("welcome to the static method - " + str(classWithStaticMethod.atr))

classWithStaticMethod.method()
x = classWithStaticMethod()
x.method()

class dirrivedClassWithStaticMethod(classWithStaticMethod):
    atr = 456

dirrivedClassWithStaticMethod.method()
x = dirrivedClassWithStaticMethod()
x.method() # static method only accesses data local to the class in which it was implemented
print()

# - class method
# class methods are a lot like static methods with two important differences. 
# A. they have a compulsory first argument (like self, though here the conventional keyword is 'cls') This refers 
#    to the class
# B. They can access attributes local to whatever dirrived class they're being used in (thanks to cls)
class classWithClassMethod:
    atr = 100

    @classmethod
    def method(cls):
        print("welcome to the class method - " + str(cls.atr))

class dirrivedClassWithClassMethod(classWithClassMethod):
    atr = 456

classWithClassMethod.method()
x = classWithClassMethod()
x.method() 
dirrivedClassWithClassMethod.method()
x = dirrivedClassWithClassMethod()
x.method()
print()








# - system methods (also called Magic Methods)
# these are methods that either come with any class, or can be filled in by the author for the system
# some are also connected to operations, eg. + or -
# to run where appropriate

#   - __init__
# this method is called when an instance of the class is being created (it's essentially a constructor)
# often attributes are created here in a fashion similar to dynamic creation (prefixed with the self keyword)
class classWith__init__:

    def __init__(self):
        print("welcome to __init__ ")

x = classWith__init__() 
print()

#   - __del__
# this method is called when an instance of the class is being deleted (it's essentially a destructor)
# This method is only run as the last operation in deleting an object, thus it is unable to access any
# attributes the object once had
class classWith__del__:

    def __del__(self):
        print("welcome to __del__ ")

x = classWith__del__() 
del(x)
print()

#   - __str__
# this method is called upon when the object needs to be converted into a human readable string (using str()
# or just the print method, etc)
class classWith__str__:

    def __str__(self):
        return "Hello human, here's the important stuff you need to know: " + str(42)

x = classWith__str__()
print(x)
print()

#   - __repr__
# this method is called upon when there is no __str__ method, or when the object is used with 'repr()'
# The purpose of this method is to return a string containing the code needed to recreate the object.
# So; in theory; obj == eval(repr(obj))
class classWith__repr__:

    def __str__(self):
        return "Hello human, here's the important stuff you need to know: " + str(8)

    def __repr__(self):
        return "classWith__repr__()"

x = classWith__repr__()
print( x )
print( repr(x) )
print( eval(repr(x)) )
print()

#   - __call__
# object.__call__(self[, args…])
# this method is run when the object is "called" like a function
class classWith__call__:

    def __call__(self, input):
        print("Welcome to the __call__ function : " + str(input))
        return "Hello"

a = classWith__call__()
print( a("HayThere") )
print()

# operators
# the following methods are run when mathematical or logical operations are done on an object
# the usual convertion is like so:  obj_a + obj_b   ->   obj_a.__add__(obj_b)
# thus, most operation methods have only two inputs (for self and the second object)
# Importantly; the operator of the first written object is run first, then the second is searched for a 'r' version of the operation
#   (this note is only really relevant in the case of binary operators)
# Binary Operators
#   +	        obj.__add__(self, other)
#   -	        obj.__sub__(self, other)
#   *	        obj.__mul__(self, other)
#   /	        obj.__truediv__(self, other)
#   //	        obj.__floordiv__(self, other)
#   %	        obj.__mod__(self, other)
#   **	        obj.__pow__(self, other[, modulo])      # this optional modulo argument can only be accessed through pow(a,b,c) which will convert to a.__pow__(b,c), which mathematically is (a^b)%c
#   <<	        obj.__lshift__(self, other)
#   >>	        obj.__rshift__(self, other)
#   &	        obj.__and__(self, other)
#   |	        obj.__or__(self, other)
#   ^	        obj.__xor__(self, other)
# the above operations come in two additional versions, 'i' and 'r'
# - i :: obj.__iadd__(self, other)
# these are activated for immediate operations, eg. a += b  
# beyond that, everything else is the same. You could just write a return from the regular version, 
# though instead you could not return anything and write the value updates within the method
# - r :: obj.__radd__(self, other)
# these are activated for situations where the object isn't the first in the written order. This only
# really makes sense in the context of working with objects of different types, eg. obj_int + obj_custom
# beyond that, everything else is the same. You can just write a return from the regular version

# Unary Operators
#   -	        obj.__neg__(self)
#   +	        obj.__pos__(self)
#   abs()	    obj.__abs__(self)
#   ~	        obj.__invert__(self)
#   complex()	obj.__complex__(self)
#   int()	    obj.__int__(self)
#   long()	    obj.__long__(self)
#   float()	    obj.__float__(self)
#   oct()	    obj.__oct__(self)
#   hex()	    obj.__hex__(self
# Comparison Operators
#   <	        obj.__lt__(self, other)
#   <=	        obj.__le__(self, other)
#   ==	        obj.__eq__(self, other)
#   !=	        obj.__ne__(self, other)
#   >=	        obj.__ge__(self, other)
#   >	        obj.__gt__(self, ot;her)
class classWithOverriddenOperators:

    def __init__(self,val):
        self.a = val

    def __str__(self):
        return str(self.a)

    def __add__(self,obj):
        # the trick is to return an object of the same type
        output = classWithOverriddenOperators(0)
        output.a = self.a + obj.a
        return output

obj_a = classWithOverriddenOperators(10)
obj_b = classWithOverriddenOperators(100)
obj_c = classWithOverriddenOperators(0)
print( obj_a,obj_b )
obj_c = obj_a + obj_b
print(obj_c)
print()







# property decorator
# this is a way of creating what looks like an attribute to an external user, but is 
# actually a method creating a value when requested
class propertyDecoratorObject:
    def __init__(self):
        self.__a = 100
        self.__b = 200
        self.__c = 300
    @property
    def value(self):
        return self.__a + self.__b + self.__c

a = propertyDecoratorObject()
print( a.value )
# a.value = 10 # this operation is not allowed
print()
# the attribute 'value' doesn't actually exist, but the method with that name is run
# when the external code attempts to access the "public attribute" 'value'








# getters/setters
# the normal way to do getting/setting in other languages would be like this
class regularGetterAndSetter:
    def __init__(self):
        self.__value = 100
    def get_value(self): 
        return self.__value
    def set_value(self,newValue):
        self.__value = newValue
#this is not nice as future usage of the class will look like this
a = regularGetterAndSetter()
b = regularGetterAndSetter()
a.set_value( a.get_value() + b.get_value() ) # <-
print(a.get_value())
print()
#we'd prefer
# a.value = a.value + b.value
#this can be achieved with the @property and @x.setter built-in decorators
class newGetterAndSetter:
    def __init__(self):
        self.__value = 100
    @property
    def value(self):
        return self.__value
    @value.setter #this line must contain the name of the value between the '@' and '.setter'
    def value(self, newValue):
        self.__value = newValue

a = newGetterAndSetter()
b = newGetterAndSetter()
a.value = a.value + b.value
print(a.value)
print()
# in this way; we can setup values as initially publically accessable, then
# rein them back in at a later date without hurting external code
# Obviously, one can write in all the getter/setter code within these methods








# Inheritance
# the process of expanding one object, creating another
# one can inherit any object, including base objects
# As with Java, all objects (unless otherwise defined) inherit from the base class, 'object'
class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):                                     # inheritance syntax
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)                   # initialization of parent class
        self.staffnumber = staffnum
    def Name(self):                                         # overriding
        return "Dr. " + self.lastname
    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber
    def doCalc(self,a,b=None,c=None):                       # sudo overloading example 1 (with a limit of three arguments)
    # in the case of this method; the positions of the default variables must be taken into account (in the expected way)
        if b:
            a += b
        if c:
            a += c
        return a
    def doCalc2(self,*a):                                   # sudo overloading example 2 (with unlimited arguments (arguments are converted into a list))
    # in the case of this method; the list-ified argument collects all the arguments that follow it, thus having arguments after this one is pointless
        output = 0
        for i in a:
            output += i
        return output   

x = Person("Brandon", "Walsh")
y = Employee("Sarah", "Ryan", "123")
print( x.Name() )
print( y.Name() )
print( y.GetEmployee() )
print( y.doCalc(1) )
print( y.doCalc(1,2) )
print( y.doCalc(1,2,3) )
print( y.doCalc2(1,2,3) )
print()







# Multiple Inheritance
class Machine:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def report(self):
        print("-running Machine method-")
        return self.name + " " + str(self.power)

class OSsoftware:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    def report(self):
        print("-running OSsoftware method-")
        return self.name + " " + str(self.version)

class computer(Machine,OSsoftware):
    def __init__(self, machineName, power, OSsoftwareName, version):
        # proper inheritance
        Machine.__init__(self, machineName, power)
        OSsoftware.__init__(self, OSsoftwareName, version) # the attribute 'name' is being overridden from Machine

        # boxed inheritance
        # this is useful, as it pushes the attributes into a scope; however you lose all the useful Inheritance stuff along the way
        # this is here until I find a good way to access the values assigned to parent classes. Hopefully it won't be much of an issue
        self.Machine = Machine(machineName, power)
        self.OSsoftware = OSsoftware(OSsoftwareName, version)

    def superReport(self):
        return computer.__bases__[0].report(self) + " " + computer.__bases__[1].report(self)

    def superReport2(self):
        return self.Machine.report() + " " + self.OSsoftware.report()

a = computer("Tluxis", 240, "Anica", 4.5)
print( a.report() ) # an overriding method wasn't defined; thus the program chose the method of the first class named in the inheritance field that has this methodå
print( a.superReport() ) # this method calls both report methods above it
print( a.superReport2() ) # this method also calls both report methods from the boxed classes
print()







# Alternate Class Creation
# there is an additional method to create a class. This method is actually used for regular class definitions, 
# but python will convert that code into code to work with this method. It's not particularly useful, though is
# important to understand metaclasses
#   type(classname, superclasses, attributedict)
# this function will subsequentally run the functon
#   type.__new__(typeclass, classname, superclasses, attributedict)
# (there is also a 'type.__init__(cls, classname, superclasses, attributedict)' method, but I'm not sure what it is for)

# regular ---- ---- ---- ---- ---- ---- ---- ----
class regularClass:
    value = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name 
# irregular ---- ---- ---- ---- ---- ---- ---- ----
Foo = type('Foo', (), {})

def func__init__(self, name):
    self.name = name
irregularClass = type(
    "irregularClass",
    (),   #   tuple([class1]) or (class1,class2)     # inheriting the 'type' class manually like this makes a metaclass, which is for a different file to talk about
    {
        "value":0,
        "__init__":func__init__,
        "sayHello":lambda self: "Hi, I am " + self.name 
    }
)

a = regularClass("Bob")
b = irregularClass("James")
print(a.sayHello())
print(b.sayHello())
print()
# both classes are identical 