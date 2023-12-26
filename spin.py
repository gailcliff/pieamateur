import sys
import os
from typing import Callable

print("gail_cliff", end='#')
print()

for arg in sys.argv:
    print('arg:', arg)

# arg = input("enter an argument: ")
# print(arg)

print(os.environ.get("PYTHONPATH"))
foo = str(8)
print(foo)

template = "My name is: {fname}. My surname is {surname}. I am {age} years old"
template2 = "My name is: %s. My surname is %s. I am %d years old"

print(template.format(fname='Clifford', surname='Odhiambo', age=21))
print(template2 % ('Gail', 'Odhiambo', 21))

for i in range(2, 200):
    for j in range(2, i):
        if i % j == 0:
            print("{i} is {factor} x {divisor}".format(i=i, factor=j, divisor=i//j))
            break
    else:
        print(f'{i} is a prime number')

print()
print()

# val = int(input("enter some: "))
val = 69

match val:
    case 0:
        print("nothing")
    case 1:
        print("something at least")
    case 2 | 3:
        print("think bigger")
    case 1000:
        print("freak")
    case _:
        print("yuh")


def signup(fname, lname, on_signup: Callable):
    username = f'{fname}_{lname}'
    on_signup(username)


def on_signed_up(username):
    print(f"{username} was signed up")


signup("clifford", "gail", on_signup=lambda usr: print(f'{usr} just got signed up'))
signup("clifford", "gail", on_signup=on_signed_up)


def time_two(number):
    def multiply(number):
        return number * 2

    return multiply(number)


print(time_two(68))

times_two = time_two
print(times_two(5))


def upperize(fn: Callable):
    return lambda: fn().upper()


def split_str(fn: Callable):
    return lambda: fn().split(" ")


def _test1():
    print("test1")


if __name__ == 'main':
    @split_str
    @upperize
    def tokenize( ):
        token = input("Enter your token:\t")
        return token


    tokenized = tokenize()
    print(tokenized)


    def upperize_with_arg(fn: Callable):
        def wrapper(string: str):
            return fn(string.upper())

        return wrapper


    @upperize_with_arg
    def tokenize_with_arg(token: str):
        return token


    to_tokenize = input("Enter string to tokenize:")
    tokenized_with_arg = tokenize_with_arg(to_tokenize)
    print(tokenized_with_arg)
