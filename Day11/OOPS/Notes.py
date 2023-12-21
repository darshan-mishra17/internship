# Object Oriented Programming
# It is a way of programming that uses classes and objects.

# Advantage is : writing resusable code. It is done by creating objects

## Main Concepts of OOPs in PYthon:
# 1. classes
# 2. Objects
# 3. Attributes
# 4. Mtehods
# 5. Inheritance
# 6. Polymorphism
# 7. Encapsulation
# 8. Data Abstraction.

# What are the real world examples of classes and objects:
"""
class: car
object 1: A red color Ford who's speed is 100km/hr
object 2: A blue color Toyota

class: Student
object1 : John, studying CSE, height 6ft
object2 : Smith, studying biology, height 5ft
"""

# What is Need of classes??
# Let say you want to track the number of students in a college who have different name and age:
# create alist where first element = student name. second element =  age
# student1 = [name, age]
# Like these there 1000 students, and each student has some other properties also like section, stream,etc
# students = [(name, age, stream,.....), (name, age, stream,.....), (name, age, stream,.....)......]
#                 student1                   student2                student3
# This way lacks origanization and it will very difficult to track all students using lists or tuples
# Thus classes are needed to oraganize the data in modular way.

# We will create a class called "Students" which will contain all attributes and methods related to each student.

# Creating a Class:
# using class keyword , then followed by classname
# class definition Syntax:
"""
class className:
    # statement1:
    .
    .
    .# statementN
"""
# For Example:
"""
class Student:
    name = "Ravi"
    age = 23
"""
    
# What are attributes ?
# Variables that belong to a class are called attributes

# How to access the attributes of a class?
# Attributes can be accessed using the dot(.) operator. Eg. ClassName.attributeName
# Attributes are public
"""
class Student:
    name = "Ravi"
    age = 23
    
print(Student.name) # Ravi
print(Student.age) # age
"""
# Creating Objects:
# Objects are created using class constructor(classname())   
# syntax:
"""
obj = className()
print(obj.attributeName)
"""
"""
class Student:
    
    # Attributes of class
    name = "Ravi"
    age = 23

stud1 = Student()  # creating object
print(stud1.name) # Ravi
print(stud1.age) # age
"""
# Methods: 
# functions that belong to class.
# functions defined within a class
# create a method that returns whether the student is studying or not
"""
class Student:
    
    #Attributes
    name = "Ravi"
    age = 23
    stream = "CSE"
    
    # methods
    def isStudying(self):
        return True
    
    
stud1 = Student() # this will create a object of class Student
print(stud1.name) # Ravi
print(stud1.age)  # 23
print(stud1.isStudying()) # True
"""

# Definition of classes:
# Class is a collection of objects.
# Class contains specific attributes(properties) and methods(functions)
# Class contains user-defined blueprints or prototype from which objects are created.


# How to create an Empty class:
"""
class Student:
    pass
"""

# Definitions of Objects:
# An object is an instance of a class.
# The object has its own state(variables/attributes) and behaviour(methods(member functions)) associated with it.
# An object contains:
# 1. State: represented by the attributes of an object(properties of object)
# 2. Behaviour: Represeneted by the methods of an object
# 3. identity : unique name given to the object to interact with other objects
"""
For examplen there is class student which contains an object student1:
# 1. state = name, age, stream
# 2. Behaviour = isStudying, isPlaying
# 3. Identity = John
"""

# Self Parameter:
# Self parameter represents the specified object of the class.
# Self parameter is used to access the attributes and the methods of class
# It binds the attributes with the given arguments
# self is used within the methods to refer the object itself
# self parameter is not received automatically rather it is passed explicitly when the method is called.
"""
class Student:
    
    #Attributes
    name = "Ravi"
    age = 23
    
    # methods
    def display(self):
        print("My name is ", self.name)
        print("My age is ", self.age)
        

stud1 = Student() # this will create a object of class Student
print(stud1.name) # Ravi
print(stud1.age)  # 23
stud1.display()
"""

# It is not mandatory to name it as "Self"
# you can give any other name
"""
class Student:
    
    #Attributes
    name = "Ravi"
    age = 23
    
    # methods
    def display(xyz):
        print("My name is ", xyz.name)
        print("My age is ", xyz.age)
        

stud1 = Student() # this will create a object of class Student
print(stud1.name) # Ravi
print(stud1.age)  # 23
stud1.display()

# But it is a good convention to name it as self
"""

    
# What is Constructor?
# A constructor is a special type of method which is called automtaically every time an object is created
# It is used to initialize the data members of class or object's state when object is created
# Like methods, a constructor can contain a collection of statements that are executed only when an object is


# Creating Constructor in Python:

# __init__ method:
# In python, the constructor is a method named __init__ that gets called when an object(instance) is created
# This __init__ is simillar to constructors in c++ and Java.
# used to initialize the attributes of object
# self represents specified instance or object that binds the attributes and given arguments
"""
class Student:
    
    # Python Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("My name is: ", self.name)
        print("My age is: ", self.age)


stud1 = Student("Ravi",23)
stud1.display()
stud2 = Student("Darshan", 22)
stud2.display()
stud3 = Student("Bharat",20)
stud3.display()
"""

# TYPES OF CONSTRUCTOR:
# 1. Non-paramterized Constructor
# It has only self as argument:
"""
class Student:
    def __init__(self):
        print("This is non-parameterized constructor")
    
    def display(self, name):
        print("My name is ",name)
        
stud1 = Student()
stud1.display("Ravi")
"""

# 2. Parameterized Constructor:
"""
class Student:
    
    # Python Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("My name is: ", self.name)
        print("My age is: ", self.age)


stud1 = Student("Ravi",23)
stud1.display()
stud2 = Student("Darshan", 22)
stud2.display()
stud3 = Student("Bharat",20)
stud3.display()
"""
# Default Constructor:
# When we don't include or declare constructor in the clas
# It doesnot perform any task. Only initialzes the attributes


class Student:
    name = "Ravi"
    stream = "CSE"
    
    def display(self):
        print("My name is",self.name)
        
stud1 = Student()
stud1.display()











