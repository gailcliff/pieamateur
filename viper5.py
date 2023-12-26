from math import pi
from pprint import pp

lst = [4,5,6,9,7,8,9]

lst.remove(6)
print(lst)
lst.reverse()

lst.extend(range(9, 20).__reversed__())
print(lst)

lst.insert(2, 8934)
print(lst)

print(lst.index(8934))

print(lst.count(9))
srtd = sorted(lst)
print(srtd)
print(lst)

cubes = [num ** 3 for num in lst]
print(cubes)

srtd_cubes = map(lambda num: num ** 3, srtd) # first arg is the function for transforming each item, second is the iterable
print(list(srtd_cubes))

lst1 = list(range(1, 9))
lst2 = lst1[:]

lst3 = [(x, y) for x in lst1 for y in lst2 if (x-y) != 1]
print(lst3)

lst4 = [name.upper() for name in ['gail', 'cliff', 'odhis']]
print(lst4)

lst5 = [lst, lst1, lst2]
print(lst5)
lst5 = [num for subgroup in lst5 for num in subgroup]
print(lst5)
print("To set: ", set(lst5))

# lst6 = [round(pi, dec_places) for dec_places in range(100)]
# for num in lst6:
#     print(num)

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

del transposed[2]
del transposed[4]
del transposed[6]
pp(transposed)

my_list = [10,20,30]
a, b, c = my_list
print(a, b, c)
my_tup = 10, 20, 30
print(my_tup)
print(type(my_tup))

s = set(reversed(range(10)))
print(s)


# dictionaries
details = {"last_name": "odhis", "first_name": "gail", "middle_name": 'cliff'}
print(list(details)) # print list of keys in the dictionaries declaring order
print(sorted(details)) # print sorted list of keys
for label, value in details.items():
    print(label, ":", value)

pp({num: num ** 3 for num in lst})

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
zipped = [[questions[i], answers[i]] for i in range(3)]

for q, a in zipped:
    print('What is your {0}? It is {1}.'.format(q, a))

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

a, b, c = [13, 23, 89]
print(a < b < c)  # returns True
