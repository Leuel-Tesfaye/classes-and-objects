# class my_class :
#      x = 5 # here x is an object 
# p1 = my_class()
# print(p1.x)

class person : # define class name person
    def __init__(self, name, age) : #? defines the constructor method def __init__  ... for class person
        self.name = name #? initializes an instance variable name with the value passed to the constructor
        self.age = age
name = input("please Enter your name:")
age = input("please enter your age : ")
p1 = person(name, age) # creates an instance (object) of person class with the name p1 

print(p1.name)
print(p1.age)
