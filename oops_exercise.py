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

# Abstruction 
# hiding internal details and showing only functionality

class Car:
    def __init__ (self):
        self.acc = False
        self.clutch = False
        self.brk = True
       
    def start(self):
        self.clutch = True
        self.acc = True
        self.brk = False
        print("car started")
        
car1 = Car()
car1.start()
        
        