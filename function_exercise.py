a = 5 
b = 10
sum  = a + b
print(sum)
# more codes 
a = 2
b = 10
sum = a + b
print(sum)
# more code
a = 1
b = 23
sum = a + b
print(sum)

def cul_add(a,b):
    add = a + b
    print(add)
    return add
# more codes 
cul_add(2,3)

# more codes line 
def culmult(a,b,c):
    multi = a * b * c
    print(multi)
    return multi
# more codes line 
culmult(2,2,2)

# more codes line 
def culsub(a,b,c,d,f,e,g,s):

    sub = a - b - c - d - f - e - g - s
    print(sub)
    return sub
    
    # more lines of codes 
culsub(2,3,46,5,3,33,5,7)

# more lines of codes 
def culdev(a,b,c):
    dev = a / b /c
    print(dev)
    return dev
    # more lines of codes 
culdev(2,3,1)
def printhello():
    print("hello")
    return print

printhello()
printhello()
printhello()
printhello()
printhello()
printhello()

def averageof3no(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
averageof3no(1,2,3)

def cul_prod(a,b):
    print(a * b)
    return a * b

cul_prod()
def cul_prod(a = 1, b = 1):
    print(a*b)
    return a * b
cul_prod()

def cul_prod(a,b=2):
    print(a*b)
    return a * b
cul_prod(1)

def cul_prod(b,a=3):
    print(a*b)
    return a * b
cul_prod(1)

questions


def cul_lenght(str):
    lenght = len(str)
    print(lenght)
    return lenght 

cul_lenght("mohd zunaid")

cities = ["delhi" , "agra", "lucknow", "mumbai", "banglore"]
heroes = ["shaktiman" , "nagraj", "batman", "supermen" , "ironmen"]

def print_lenght(list):
    print(len(list))
    return len(list)

print_lenght(cities)
print_lenght(heroes)

def print_lenght(list):
    print(len(list))
    return len(list)

print_lenght("mohd")
print_lenght("zunaid")
print_lenght("mohdzunaid")
print_lenght("mohdzunaid1234")
print_lenght("mohd zunaid")

print(heroes[0], end=" ")
print(heroes[1], end=" ")
def print_list(list):
    for i in list:
        print(i, end=" ")
        
print_list(heroes)

n = 5
    
def find_fact(a,b):
    
def print_function():
    print("hello world ")
    return print
print_function()
print_function()
print_function()
print_function()

def print_name(name):
    print(f"hello, {name}")
    
print_name("mohd zunaid")
def geet_user(name):
    print(f"hello, {name}")
    
geet_user("mohd zunaid")

def find_squre(n):
    for i in range(1,n+1):
        print(f"sqare of {i} is {i*i}")
        
find_squre(10)

def find_square(n):
    print(n*n)
find_square(5)

def find_evenorodd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
        return n
find_evenorodd(3)

list = [1,2,3,4,5,6,7,8,9,10]

def sum_of_list(list):
    print(sum(list))
    
sum_of_list(list)

def find_max(list):
    print(max(list))
    
find_max(list)

def find_maxofthree(a,b,c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)
        return a,b,c
find_maxofthree(3,7,2)

def reverse_string(str):
    print(str[::-1])
    return str 

reverse_string("mohd zunaid")

def find_factorial(n):
    fact = 1
    for i  in range(1,n+1):
     fact *= i
    print(fact)
    
find_factorial(5)
    
    
def is_palindrome(str):
    if str == str[::-1]:
        print("palindrome")
        
    else:
        print("not palindrome")
        
    return str
is_palindrome("madam")

def find_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    print(fact)
    
    
find_fact(5)

def find_inr(USD):
    INR = USD * 83
    print(USD, "doller is equal to", INR, "INR")
    
    
find_inr(100)


str1 = "EVEN"
str2 = "ODD"

def even_odd(n):
    if n%2==0:
        print(str1)
    else:
        print(str2)
        return n
even_odd(3)

recursion function
n = 5
def show(n):
    # if (n==0): # base condition
    #     return
    print(n)
    show(n-1)# work
    
show(5)

n = 5
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
show(5)

 recurstion function for factorial

def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        fact = n * factorial(n-1)
        print(fact)
        return fact
    
factorial(6)


def cal_sumofn(n):
    if n == 0:
        return 0
    else:
        sum = n + cal_sumofn(n-1)
        print(sum)
        return sum
cal_sumofn(5)


def nsum(n):
    if n == 0:
        return 0
    else:
        return n + nsum(n-1) 
    print(n)
nsum(5)

def calc_sum(n):
    if n == 0:
        return 0
    else:
        return calc_sum(n-1) + n
    
sum = calc_sum(5)
print(sum)

list = [1,2,3,4,5]
def print_list(list):
    if len(list) == 0:
        return
    else:
        print(list)
        
print_list(list)

def print_list(list,inx = 0):
    if (inx == len(list)):
        return
    
    print(list[inx])
    print_list(list, inx + 1)
li = [1,2,3,4,5]
    
print_list(li)
