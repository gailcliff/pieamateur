from typing import overload
from pprint import pp


def foo(*, bar, baz, chaz):
    print(bar, baz, chaz)


foo(baz=4, bar="Yay", chaz=True)


my_ints = [5,43,644,23,2,321]
my_ints2 = [i for i in range(10)]

# my_ints_3 = [(x, y) for y in my_ints2 for x in my_ints]
# pp(my_ints_3)

my_ints4 = map(lambda num: num ** 2, my_ints)
print(list(my_ints4))

nested_list = [
    range(0, 10),
    range(10, 20),
    range(20, 30),
    range(30, 40),
    range(40, 50),
]
nested_list = [list(segment) for segment in nested_list]
transposed = [[segment[i] for segment in nested_list] for i in range(10)]
pp(nested_list)
pp(transposed)
flattened = [num for chunk in nested_list for num in chunk]
print(flattened)

