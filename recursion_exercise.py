# def print_1_to_n(n):
#     if n == 0:
#         return
#     print_1_to_n(n - 1)
#     print(n)

# print_1_to_n(5)
# This will print numbers from 1 to n in ascending order.
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

print_n_to_1(5)


def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))
