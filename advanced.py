from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
print(cache.get(2))


import time

def time_check(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start)
    return wrapper

@time_check
def task():
    for i in range(1000000):
        pass

task()
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for ch in "ABCDE":
        print(ch)
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
print("Done")
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)
class Employee:
    def salary(self):
        return 20000

class Developer(Employee):
    def salary(self):
        return 50000

emp = Developer()
print(emp.salary())
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(10))
import re

def check_password(password):
    if (len(password) >= 8 and
        re.search("[A-Z]", password) and
        re.search("[a-z]", password) and
        re.search("[0-9]", password)):
        return "Strong Password"
    return "Weak Password"

print(check_password("Python123"))
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rotated = list(zip(*matrix[::-1]))
print(rotated)
tasks = []

while True:
    print("1.Add 2.View 3.Delete 4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        tasks.append(input("Task: "))
    elif choice == "2":
        print(tasks)
    elif choice == "3":
        tasks.pop(int(input("Index: ")))
    elif choice == "4":
        break
