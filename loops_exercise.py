i = 1
while i<=5:
  
    print("hello")
#     i += 1
i = 5
while i >= 1:
#     print(i)
#     i -= 1

i = 1
while i <= 10:
    print(i)
    i = i + 1
      
      
i = 10 
while i >= 1:
    print(i)
    i -= 1


i = 1
while i <= 100:
    print(i)
    i += 1


i = 100 
while i >= 1:
    print(i)
    i -= 1
n = int(input("enter a number :"))
i = 1 
while i <= 10:
    print(i*n)
    i += 1

i = 1
while i <= 10:
    print(i*i)
    i += 1

heros = ["spider" , "ironman", "thor", "hulk", "captain america"]
x = "hulk"
ind = 0 
while ind < len(heros):
    if (heros[ind] == x):
        print("found hulk")
        break
    else:
        print("findind...")
    ind += 1
    num  = [1,2,3,4,5,6,7,8,9,10]
x =  4
inx = 0
while inx < len(num):
    if (num[inx] == x):
        print("found")
        break    
    else:
#         print("not found")
        inx += 1 
        
i = 0 
while i <= 5:
        if (i == 3):
         i +=1
         continue
        print(i)
        i += 1
break

for i in range(34):
        if (i==30):
         break
        print(i)
        
        
# continue 
for  i in range(12):
        if i==0:
                continue
#         print(i)
i = 0
while i <= 12:
        i += 1
        if i==6:
                continue
        elif i==8:
                continue
        
        if i==11:
                break
        print(i)  

# for loop 
for i in range(10):
        print(i)
for i in range(1,11):
        print(i)
        
for i in range(1,21,2):
        print(i)

# with python 

fuirt = ["apple", "banana", "mango", "grapes"]
for i in fuirt:
        print(i)

# with string
name  = "mohd zunaid"
print(len(name))
for i in name:
        print(i)
       
       
colour = ["red", "green", "blue", "yellow"]
for index, i in  enumerate(colour):
        print(index, i)

for i in range(1, 11):
        for j in range(1,11):
                print(i, j)
       
         whike loop 
i = 0
while i< 5:
        i += 1
        print(i)

i = 2 
while i <=10:
        print(i)
        i += 2
else:
        print("loop is ended")
        
        for i in range(1,11):
                if i==5:
                 continue 
                elif i ==6:
                        continue
                if i==9:
                        break
                
        print(i)


str = "mohdzunaid"
for i in str:
         if (i=='i'):
                 break
         print(i)
         
print("END loop")

str = "mohdzunaid"
for i in str:
         if (i=='i'):
                continue
         print(i)
         
print("END loop")
# pratice question

 
# list = [1,4,9,16,25,36,49,64,81,100]
# for i in list:
#         if

# i = 0
# while i<10:
#         i +=1
#         print(i*i)
# list = []
# print(list)
        
        
list = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter A number :"))
for i in list:
        if (i==x):
                print("found x here" )
                continue
        print(i)
        
list = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter A number :"))
for i in list:
        if (i==x):
                print("found x here")
                break
        print(i)

for i in range(1,101):
        print(i)
        
        
for i in range(101,0, -1):
        print(i)

n = int(input("enter a number ;"))
for i in range (1,11,1):
        print(i*n)


for i in range(5):
        pass
if i==3:
        pass
        
        
# print("some important code")


# n = int(input("enter a number :"))
# sum = 0
# for i in range(1,n+1):
#         sum += i
#         print(sum)
       
n = int(input("enter a number :"))  
sum = 0 
i = 1

while i <= n:
        i += 1
        sum += i 
        print(sum)
         
         
         
         
n = 5
fac = 1
i = 1

while i <= n:
        i += 1
        fac *= i 
       
        print(fac)

fac = 1
n = int(input("enter a number :"))
for i in range(1,n+1):
        fac *= i 
        print(fac)