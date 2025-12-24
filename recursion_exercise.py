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
#         return 1
#     return x * power(x, n - 1)

# print(power(2, 5))


# def count_digits(n):
#     if n == 0:
#         return 0
#     return 1 + count_digits(n // 10)

# print(count_digits(12345))

# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return (n % 10) + sum_of_digits(n // 10)

# print(sum_of_digits(123))
# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# print(reverse_number(1234))


# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# print(reverse_number(1234))


def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)

print(is_palindrome("madam", 0, 4))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))


def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 0, len(arr) - 1, 7))

def is_sorted(arr, index):
    if index == len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)

print(is_sorted([1, 2, 3, 4, 5], 0))


def find_max(arr, index):
    if index == len(arr) - 1:
        return arr[index]
    return max(arr[index], find_max(arr, index + 1))

print(find_max([3, 7, 2, 9, 5], 0))
