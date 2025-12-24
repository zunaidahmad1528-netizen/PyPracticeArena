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


def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(123))
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print(reverse_number(1234))


def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print(reverse_number(1234))
