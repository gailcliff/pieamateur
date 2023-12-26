
# def prime_range(lower_bound: int, upper_bound: int):
#     primes = []
#     for i in range(lower_bound, upper_bound+1):
#         for j in range(lower_bound, i):
#             if i % j == 0:
#                 print(f"{i} divided by {j} = {i//j} remainder {i%j}")
#                 break
#         else:
#             print(f"{i} is a prime number")
#             primes.append(i)
#
#     return primes


# print("Enter a lower bound and upper bound to list all prime numbers in that range...")
# i = input("\tEnter lower bound: ")
# j = input("\tEnter upper bound: ")
# print("Primes: ", prime_range(int(i), int(j)))


# ----------------------


# nums_str = input("Enter nums: ")
# nums = [int(i) for i in nums_str.strip().split(sep=' ')]
# # nums = (2,3,5,7,11,4565566,34,2,543,32)
#
# match nums:
#     case (2, 3, 5, *rest):
#         print("sequence of prime numbers")
#     case (2, 4, 6, *_):
#         print("sequence of even numbers")
#     case (1, 3, 5, 7, *_):
#         print("sequence of odd numbers")
#     case _:
#         print("other type of sequence")


# --------------------------

# from enum import Enum
#
#
# class Color(Enum):
#     R = 'red'
#     G = 'green'
#     B = 'blue'
#
#     def __str__(self):
#         return self.value
#
#
# clr = Color.R
# print(clr.name)


from typing import Callable


def to_upper_case(fn: Callable):
    return lambda: fn().upper()


def chop_it_up(fn: Callable):
    return lambda: fn().split(" ")


@chop_it_up
@to_upper_case
def input_and_transform():
    foo = input("Enter a phrase:\t")
    return foo


print(input_and_transform())


def capitalize_and_split(fn: Callable):
    return lambda word: fn(word.upper().split(),)


@capitalize_and_split
def capt(word: str,):
    return word


bar = capt("gail cliff",)
print(bar)
