list = [2, 3, 4]
list.append(6)
print(list)

name = ["jonh", "doe", "jane"]
name.append("zunaid")
print(name)

list = [2,5,2,4,2,4,1,6,9,7,10,11]
list.sort()
print(list)

list = [2, 5, 2, 4, 2, 4, 1, 6, 9, 7, 10]
list.append(11)
list.sort(reverse=True)
print(list)

list = [2, 5, 2, 4, 2, 4, 1, 6, 9, 7, 10]
list.append(11)
list.sort()
print(list)

for(i = 0; i<34; i++)
print(i)

list = [2, 5, 2, 4, 2, 4, 1, 6, 9,]
list.reverse()
print(list)

list = ["a", "b", "c", "d", "e"]
list.reverse()
print(list)

list = [2, 5, 2, 4, 2, 4, 1, 6, 9]
list.insert(0,6)
print(list)

list = [2, 5, 2, 4, 2, 4, 1, 6, 9]
list.remove(2)
print(list)

list = [2, 5, 2, 4, 2, 4, 1, 6, 9]
list.pop(1)
print(list)


# 1. Find GCD (Greatest Common Divisor) using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6


# 2. Check if a string is a palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
     return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False


# 3. Count ways to climb stairs (like Fibonacci)
def climb_stairs(n):
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(climb_stairs(5))  # Output: 8


# 4. Generate all subsets of a set
def subsets(nums, index=0, current=[]):
    if index == len(nums):
        print(current)
        return
    # Include current element
    subsets(nums, index + 1, current + [nums[index]])
    # Exclude current element
    subsets(nums, index + 1, current)

subsets([1, 2, 3])


# 5. Solve Maze Pathfinding (DFS recursion)
def solve_maze(maze, x, y, path):
    if x == len(maze)-1 and y == len(maze[0])-1:
        print(path)
        return
    if x+1 < len(maze) and maze[x+1][y] == 1:
     solve_maze(maze, x+1, y, path + "D")  # Down
    if y+1 < len(maze[0]) and maze[x][y+1] == 1:
        solve_maze(maze, x, y+1, path + "R")  # Right

maze = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]
solve_maze(maze, 0, 0, "")
