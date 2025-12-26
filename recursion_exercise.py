# def print_1_to_n(n):
#     if n == 0:
#         return
#     print_1_to_n(n - 1)
#     print(n)

# print_1_to_n(5)
# This will print numbers from 1 to n in ascending order.
# def print_n_to_1(n):
#     if n == 0:
#         return
#     print(n)
#     print_n_to_1(n - 1)

# print_n_to_1(5)


# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)

# print(sum_n(5))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))
# # This will print numbers from n to 1 in descending order.


# def power(x, n):
#     if n == 0:
# #         return 1
# #     return x * power(x, n - 1)

# # print(power(2, 5))


# # def count_digits(n):
# #     if n == 0:
# #         return 0
# #     return 1 + count_digits(n // 10)

# # print(count_digits(12345))

# # def sum_of_digits(n):
# #     if n == 0:
# #         return 0
# #     return (n % 10) + sum_of_digits(n // 10)

# # print(sum_of_digits(123))
# # def reverse_number(n, rev=0):
# #     if n == 0:
# #         return rev
# #     return reverse_number(n // 10, rev * 10 + n % 10)

# # print(reverse_number(1234))


# # def reverse_number(n, rev=0):
# #     if n == 0:
# #         return rev
# #     return reverse_number(n // 10, rev * 10 + n % 10)

# # print(reverse_number(1234))


# def is_palindrome(s, start, end):
#     if start >= end:
#         return True
#     if s[start] != s[end]:
#         return False
#     return is_palindrome(s, start + 1, end - 1)

# print(is_palindrome("madam", 0, 4))


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(48, 18))


# def binary_search(arr, low, high, key):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if arr[mid] == key:
#         return mid
#     elif key < arr[mid]:
#         return binary_search(arr, low, mid - 1, key)
#     else:
#         return binary_search(arr, mid + 1, high, key)

# arr = [1, 3, 5, 7, 9]
# print(binary_search(arr, 0, len(arr) - 1, 7))

# def is_sorted(arr, index):
#     if index == len(arr) - 1:
#         return True
#     if arr[index] > arr[index + 1]:
#         return False
#     return is_sorted(arr, index + 1)

# print(is_sorted([1, 2, 3, 4, 5], 0))


# def find_max(arr, index):
#     if index == len(arr) - 1:
#         return arr[index]
#     return max(arr[index], find_max(arr, index + 1))

# print(find_max([3, 7, 2, 9, 5], 0))


# def flatten_list(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(flatten_list(item))
#         else:
#             result.append(item)
#     return result

# print(flatten_list([1, [2, [3, 4]], 5]))


# def multiply(a, b):
#     if b == 0:
#         return 0
#     return a + multiply(a, b - 1)

# print(multiply(4, 5))


# def tower_of_hanoi(n, src, helper, dest):
#     if n == 1:
#         print(f"Move disk 1 from {src} to {dest}")
#         return
#     tower_of_hanoi(n - 1, src, dest, helper)
#     print(f"Move disk {n} from {src} to {dest}")
#     tower_of_hanoi(n - 1, helper, src, dest)

# tower_of_hanoi(3, 'A', 'B', 'C')
# def count_ways_to_climb(n):
#     if n == 0 or n == 1:
#         return 1
#     return count_ways_to_climb(n - 1) + count_ways_to_climb(n - 2)

def permutations(s, step=0):
    if step == len(s):
        print("".join(s))
    for i in range(step, len(s)):
        s_copy = [c for c in s]
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        permutations(s_copy, step + 1)

permutations(list("ABC"))


# 2. N-Queens Problem (place N queens on an NxN chessboard)
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_n_queens(n, row + 1, board + [col])

solve_n_queens(4)

# 3. Subset Sum Problem
def subset_sum(nums, target, index=0, current=[]):
    if target == 0:
        print(current)
        return
    if index >= len(nums):
        return
    # Include current number
    subset_sum(nums, target - nums[index], index + 1, current + [nums[index]])
    # Exclude current number
    subset_sum(nums, target, index + 1, current)

subset_sum([2, 4, 6, 10], 16)


def exist(board, word):
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c]:
            return False
        temp, board[r][c] = board[r][c], "#"
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        board[r][c] = temp
        return found
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True
    return False

grid = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
print(exist(grid, "ABCCED"))  # True
print(exist(grid, "SEE"))     # True
print(exist(grid, "ABCB"))    # False
