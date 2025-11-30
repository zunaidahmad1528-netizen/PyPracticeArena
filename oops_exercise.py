# class Students:
#     name = "zunaid"
# s1 = Students()
# print(s1.name)

# s2 = Students()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"
#     name = "new car"
# car1 = Car()
# print(car1.color)
# print(car1.brand)
# print(car1.name)


# # more codes od line
# class Students():
#     name  = "zunaid"
#     def __init__():
#         print("adding new students in database..")
# s1 = Students()
# print(s1)
# class Students:
    
#     def __init__(self):
#         print(self)
#         print("adding new student in database..")
        
# s1 = Students()

# class Students:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new students in database..")
        
# s1 = Students("zunaid")
# print(s1.name)
# s2 = Students("mohd")
# print(s2.name)
        
# class Students:
#     def __init__(self,name,marks,age,sex):
#         self.name = name
#         self.marks = marks
#         self.age = age
#         self.sex = sex
#         print("adding some or more data..")
        
# s1 = Students("zunaid", 97 , 19 , "male")
# print(s1.name, s1.marks , s1.age , s1.sex)

# s2 = Students("rihan", 89 , 19 , "i dont know may be he is a gay")
# print(s2.marks , s2.age , s2.name , s2.sex)

# class Car:
#     name = "toyota"
#     colour = "red"
#     size = "large"
    
# s1 = Car()
# print(s1)

# class Car:
#     name = "swift"
#     colour = "black"
#     size = "medium"
#     model = 2025
# s1 = Car()
# s2 = Car()
# s3 = Car()
# s4 = Car()
# s5 = Car()
# print(s1.name)
# print(s2.name)
# print(s3.name)
# print(s4.name)
# print(s5.name)
# print(s1.colour)
# print(s2.colour)
# print(s3.colour)
# print(s2.colour ,s2.colour)
# class Student:
#     name = "zunaid"
#     marks = 97
#     age = 19
    
# s1 = Student()
# s2 = Student()
# print(s1.name , s1.marks , s1.age)
# print(s2.name , s2.marks , s2.age)
# class Student:
#     # default constructor
#     def __init__(self):
    
    
#     # parameterized constructor
#      def __init__(self, name , marks , age ):
#         self.name = name
#         self.marks = marks
#         self.age = age
#         print("student data added successfully")
        
# s1 = Student("mohd zunaid" , 85 , 19)
# print(s1.name , s1.age , s1.marks)

# s2 = Student("mohd rihan" , 89 , 19)
# print(s2.name , s2.age , s2.marks)
# class Office:
#      company = "ABC Pvt Ltd"
#      def __init__(self, emp_name, emp_id, emp_salary, emp_experence):
       
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         self.emp_experence = emp_experence
        
        
# emp1 = Office("Mohd zunaid", "A101", 50000, "2 years")
# emp2 = Office("Mohd rihan", "A102", 60000, "3 years")
# emp3 = Office("Mohd asad", "A103", 55000, "2.5 years")
# print(emp1.emp_name, emp1.emp_id, emp1.emp_salary, emp1.emp_experence, emp1.company)
# print(emp2.emp_name, emp2.emp_id, emp2.emp_salary, emp2.emp_experence, emp2.company)
# print(emp3.emp_name, emp3.emp_id, emp3.emp_salary, emp3.emp_experence, emp3.company)
# print("Employee data added successfully")

# # Question: Create a class Student with attributes and print them using an object.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Rahul", 20)

# print("Name:", s1.name)


# # Question: Create a class Car with a method that displays car details.
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def show(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)

# c1 = Car("Toyota", "Fortuner")
# c1.show()



# class Student:
#     school = "XYZ high school"
#     def __init__(self, name, marks, age):
#         self.name = name
#         self.marks = marks
#         self.age = age
#         print("Student data added successfully")
    
#     def data(self):
#         print("Student Name:", self.name , self.marks , self.age , self.school)
#     def getmarks(self):
#         return self.marks
        
# s1 = Student("Mohd zunaid", 97, 19)
# print(s1.name, s1.marks, s1.age, s1.school)
# s2 = Student("Mohd rihan", 89,19)
# print(s2.name, s2.marks, s2.age, s2.school)

# s1.data()
# s2.data()
# print(s1.getmarks())
# print(s2.getmarks())

       
# class Student:
#     def __init__(self, name, physics, chemistry, math):
#       self.name = name
#       self.physics = physics
#       self.chemistry = chemistry
#       self.math = math
    
#     def student_info(self):
#         return (self.name, self.physics, self.chemistry, self.math)
        
    
#     def average_marks(self):
#         return (self.physics + self.chemistry + self.math)/3
    
      
      
      
# s1 = Student("zunaid", 97, 95, 98)
# print(s1.name, s1.physics, s1.chemistry, s1.math)
# print("Student Info:", s1.student_info())
# print("Average Marks:", s1.average_marks()) 


# # static methods 
# # methods that dont use self parameter (work at class level)
# # so we use @staticmethod decorator to define static methods

# class Student:
#     school = "XYZschool"
    
#     def __init__(self, name, marks):
#       self.name = name
#       self.marks = marks
    
    
#     @staticmethod
    
#     def hello():
#       print("hello")
    
      
      
# s1 = Student("zunaid",97)
# print(s1.name, s1.marks, s1.school)

# s1.hello()

# # Abstruction 
# # hiding internal details and showing only functionality

# class Car:
#     def __init__ (self):
#         self.acc = False
#         self.clutch = False
#         self.brk = True
       
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         self.brk = False
#         print("car started")
        
# car1 = Car()
# car1.start()
        

# Encapsulation
# wrapping data and functions into a single unit(object).


# class Account:
#     def __init__(self, balance, account_number):
#         self.balance = balance
# #         self.account_number = account_number
        
#         # debit method
#     def debit(self, account):
#         self.balance -= account
#         print("Rs.", account, "debited from your account.")
#         print("Your current balance is:" , self.balance)
#         # credit method
#     def credit(self, account):
#         self.balance += account
#         print("Rs.", Account, "credited to your account..")
#         print("Your current balance is:" , self.balance)
        
# acc1 = Account(50000, 2463265772002)
# print(acc1.balance, acc1.account_number)
# acc1.debit(5000)
# acc1.credit(10)
        
        
# a, b = input("Enter two numbers: ").split()
# a = int(a)
# # b = int(b)
# print("Python", "Java", "C++", sep=" | ")
# name = "Bob"
# age = 30
# print(f"{name} is {age} years old")
# print(f"Next year: {age + 1}")

# name = "Bob"
# age = 30
# print("{} is {} years old".format(name, age))
# name = "Bob"
# age = 30
# print("%s is %d years old" % (name, age))
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# salary = float(input("Enter your salary: "))

# Display output
# print("\n--- User Info ---")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Salary: ${salary:.2f}")
# print(f"Next year you'll be {age + 1} years old")

# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("zunaid")
# print(s1.name)
# del s1.name
# # print(s1.name)

# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("zunaid")
# del s1
# print(s1)

# class Details:
#     def __init__(self, account_number, account_password):
#         self.account_number = account_number
#         self.__account_password = account_password
        
#     def reset_password(self):
#         print(self.__account_password)
# acc1 = Details("2463265772002", "zunaid123")
# print(acc1.account_number)
# print(acc1.reset_password())

# class Person:
#     __name = "anonymous"
    
#     def __hello(self):
#         print("Hello person")
        
#     def welcom(self):
#        self.__hello()
# p1 = Person()
# print(p1.welcom())


# ###  INHERITANCE


# class Car:
#     @staticmethod
#     def start():
#         print("car started")
        
#     def stop():
#         print("car atoppedd")

# class ToyotaCar(Car):
#     def __init__ (self, name):
#         self.name = name
        
# car1 = ToyotaCar("FORTUNER")
# car2 = ToyotaCar("INNOVA")

# print(car1.name)
# print(car1.start())

# single level inheritance


# class Bike:
#     @staticmethod
#     def start():
#         print("Bike started..")
        
#     @staticmethod
#     def accelearte():
#         print("Bike is ready to accelearte..")
        
#     @staticmethod
#     def stop():
#         print("Bike stopped..")
# class JavaBike(Bike):
#     def __init__ (self, name):
#         self.name = name
# bike1 = JavaBike("JavaBike15")
# print(bike1.name)
# print(bike1.start())
# print(bike1.accelearte())
# print(bike1.stop())

# class Animal:
#     colour = "yellow"
#     height = "5 feet"
#     @staticmethod
#     def speak():
#         print("Animal speaks")
    
#     @staticmethod
#     def walk():
#         print("Animalwalks")
    
#     @staticmethod
#     def eat():
#         print("Animal eats")
        
#     @staticmethod
#     def sleep():
#         print("Animal sleeps")
        
#     @staticmethod
#     def run():
#         print("Animal runs")

# class Lion(Animal):
#     def __init__ (self, name):
#         self.name = name
# lion1 = Lion("African Lion")
# print(Lion.colour)
# print(Lion.height)
# print(lion1.name)
# print(lion1.speak())
# print(lion1.walk())
# print(lion1.eat())
# print(lion1.sleep())
# print(lion1.run())


# multi level inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")
    
#     @staticmethod
#     def accelearte():
#         print("car is ready to accelearte...")
        
#     @staticmethod
#     def stop():
#         print("car stopped...")
        
# class ToyotaCar(Car):
#     def __init__ (self, brand):
#         self.brand = brand
    
# class FortunerCar(ToyotaCar):
#     def __init__ (self, type, colour, model):
#         self.type = type
#         self.colour = colour
#         self.model = model
# for1 = FortunerCar("Suv", "black", 2025)
# print(for1.type)
# print(for1.colour)
# print(for1.model)
# for1.start()
# for1.accelearte()
# for1.stop()
# for1.brand = "Toyota"
# print(for1.brand)




# multiple inheritance


# class A:
#     varA = "I am class A"
# class B:
#     varB = "I am class B"
# class C(A, B):
#     varC = "I am class C"
# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#  SUPER METHOD
# super() method is used to access methods of the parent class.

# class Car:
#     def __init__ (self, type):
#         self.type = type
    
#     @staticmethod 
#     def start():
#         print('car started...')
     
#     @staticmethod   
#     def stop():
#         print("car stopped...")
    
# class ToyotaCar(Car):
#     def __init__ (self, model, name, type):
#         self.name = name
#         self.model = model
#         super().__init__(type)
        
        
# car1 = ToyotaCar("2025", "Fourtuner", "suv")
# print(car1.name)
# print(car1.type)
# print(car1.model)
# car1.start()
# car1.stop()


# class Student:
#     def __init__ (self, name):
        
#      self.name = name
#     @staticmethod
#     def greet():
#          print("hello student")
#     @staticmethod
#     def bye():
#         print("bye student")
        
# class StudentDetails(Student):
#     def __init__ (self, name, marks, age):
#         self.marks = marks
#         super().__init__(name)
#         self.age = age
        
# student1 = StudentDetails("zunaid", 97, 19)
# Student.greet()
# print(student1.name)
# print(student1.age)
# print(student1.marks)
# Student.bye()
    
# class Animal:
#     def __init__ (self, species):
#         self.species = species
#     @staticmethod
#     def eat():
#         print("Animal eats")
#     @staticmethod
#     def sleep():
#         print("Animal sleeps")
#     @staticmethod
#     def run():
#         print("Animal runs")
# class Info(Animal):
#     def __init__ (self, breed, species):
#         self.breed = breed
#         super().__init__(species)
# animal1 = Info("Lion", "Mammal")       
   
# print(animal1.breed)
# print(animal1.species)
# Animal.eat()
# Animal.sleep()
# Animal.run()
        
        
# class Person:
#     def __init__ (self, name , age , date_of_birth):
#         self.name = name
#         self.age = age
#         self.date_of_birth = date_of_birth
#     @staticmethod
#     def greet():
#         print("Hello :" "zunaid")
#     @staticmethod
#     def Bye():
#         print("Bye have a nice day")
# class employee(Person):
#     def __init__ (self, name, age, date_of_birth, emp_id, emp_salary):
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         super().greet()
#         super().__init__(name, age, date_of_birth)
# employee1 = employee("zunaid", 19, "01-01-2005", "A101", 50000)
# Person.greet()
# print(employee1.name)
# print(employee1.age)
# print(employee1.date_of_birth)
# print(employee1.emp_id)
# print(employee1.emp_salary)
# Person.Bye()


# print("End of oops_exercise.py")

# class Person:
#     name = "ananymous"
#     def __init__ (self, name):
#         self.name = name
        
# p1 = Person
# p1.name = "zunaid"
# print(p1.name)


# class method 
# class Person:
#     name = "ananymous"
#     def change_name(self, name):
#         self.name = name
# p1 = Person()
# p1.change_name("zunaid")

# print(p1.name)
# print(Person.name)

# class Person:
#     name = "ananymous"
    
#     def change_name(self, name):
#         Person.name = name
        
# p1 = Person()
# p1.change_name('zunaid')
# print(p1.name)
# print(Person.name)
        
        
# class Person:
#     name = "ananymous"
#     def change_name(self, name):
#         self.__class__.name = name
# p1 = Person()
# p1.change_name("zunaid")
# print(p1.name)
# print(Person.name)

# class Person:
#     name = "ananymous"
#     def change_name(self, name):
#         self.__class__.name = name
        
# p1 = Person()
# print(p1.name)
# p1.change_name("zunaid")
# print(Person.name)
# print(p1.name)