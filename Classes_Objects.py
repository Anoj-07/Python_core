class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} \nand I am {self.age} years old. "
    
p1 = Person("Anoj", 22)

print(p1.introduce()) 