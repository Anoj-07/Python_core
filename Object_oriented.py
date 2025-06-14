# '''
# What we will learn in this topic:
# What classes and objects are

# How to define classes and create objects

# Understanding the __init__ constructor method

# Adding methods to a class

# '''

# Short Notes:
# Classes are blueprints for objects. Objects are instances of classes. __init__ initializes an object’s attributes.

class Person: 
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    
    def greet(self):
        print(f"Hi, I am {self.name} and i am {self.age} year old.")

person_1 = Person("dear Paru", 22)
person_1.greet()