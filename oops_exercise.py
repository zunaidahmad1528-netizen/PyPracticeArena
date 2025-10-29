class Students:
    name = "zunaid"
s1 = Students()
print(s1.name)

s2 = Students()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"
    name = "new car"
car1 = Car()
print(car1.color)
print(car1.brand)
print(car1.name)


# more codes od line
class Students():
    name  = "zunaid"
    def __init__():
        print("adding new students in database..")
s1 = Students()
print(s1)
class Students:
    
    def __init__(self):
        print(self)
        print("adding new student in database..")
        
s1 = Students()

class Students:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new students in database..")
        
s1 = Students("zunaid")
print(s1.name)
s2 = Students("mohd")
print(s2.name)
        
class Students:
    def __init__(self,name,marks,age,sex):
        self.name = name
        self.marks = marks
        self.age = age
        self.sex = sex
        print("adding some or more data..")
        
s1 = Students("zunaid", 97 , 19 , "male")
print(s1.name, s1.marks , s1.age , s1.sex)

s2 = Students("rihan", 89 , 19 , "i dont know may be he is a gay")
print(s2.marks , s2.age , s2.name , s2.sex)

class Car:
    name = "toyota"
    colour = "red"
    size = "large"
    
s1 = Car()
print(s1)

class Car:
    name = "swift"
    colour = "black"
    size = "medium"
    model = 2025
s1 = Car()
s2 = Car()
s3 = Car()
s4 = Car()
s5 = Car()
print(s1.name)
print(s2.name)
print(s3.name)
print(s4.name)
print(s5.name)
print(s1.colour)
print(s2.colour)
print(s3.colour)
print(s2.colour ,s2.colour)
class Student:
    name = "zunaid"
    marks = 97
    age = 19
    