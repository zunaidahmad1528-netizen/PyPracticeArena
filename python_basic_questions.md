# Python Basic Questions and Answers

## 1. What is Python?
Python is a high-level, interpreted, and beginner-friendly programming language used for web development, automation, data analysis, AI, scripting, and more.

## 2. What are variables in Python?
Variables are containers used to store data values.

```python
age = 25
name = "Aman"
print(age, name)
```

## 3. What is the difference between a list and a tuple?
A list is mutable, while a tuple is immutable.

```python
numbers = [1, 2, 3]   # list
nums = (1, 2, 3)      # tuple
numbers.append(4)
print(numbers)
```

## 4. What is a dictionary in Python?
A dictionary stores data in key-value pairs.

```python
student = {"name": "Rahul", "age": 21}
print(student["name"])
```

## 5. What is a function in Python?
A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
    return a + b

print(add(3, 5))
```

## 6. What is an if-else statement?
It is used to make decisions in a program.

```python
num = 10
if num > 0:
    print("Positive")
else:
    print("Not positive")
```

## 7. What is a loop?
A loop repeats a block of code multiple times.

```python
for i in range(1, 4):
    print(i)
```

## 8. What is the difference between append() and extend()?
`append()` adds one item, while `extend()` adds multiple items.

```python
my_list = [1, 2]
my_list.append(3)
my_list.extend([4, 5])
print(my_list)
```

## 9. What is slicing?
Slicing is used to access a portion of a string, list, or tuple.

```python
word = "Python"
print(word[0:3])
```

## 10. What is the difference between a for loop and a while loop?
A for loop is used when the number of iterations is known, while a while loop continues until a condition becomes false.

```python
for i in range(3):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1
```

## Summary
Python basics include variables, data types, functions, loops, conditions, and collections such as lists, tuples, sets, and dictionaries.

These are common beginner-level questions for practice and interviews.
