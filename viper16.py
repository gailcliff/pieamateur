from datetime import date, datetime

class DivErr(Exception):

    def __str__(self):

        return "div by 0 h0"


def div(x, y):
    if y == 0:
        raise DivErr

    return x/y


try:
    a = div(3,0)
except DivErr as e:
    print(e)
else:
    print(f"div result: {a}")
finally:
    print("computation done")

today = datetime.today()
print(today.year, today.month, today.day, today.ctime())

now = datetime.now()
print(now.hour, now.minute, now.second, now.ctime())


class Person:

    hobbies: list  # this will be shared by all instances
    age: int

    def __init__(self, name):
        self.name = name
        self.hobbies = []


person = Person("john doe")
person.hobbies.append("skiing")
person.hobbies.append("travel")

person1 = Person("janet jane")
person1.hobbies.append("swimming")
person1.hobbies.append("archery")

print(person.hobbies)  # ['skiing', 'travel', 'swimming', 'archery']
print(person1.hobbies)  # ['skiing', 'travel', 'swimming', 'archery']


from enum import Enum
from dataclasses import dataclass


class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'

    def __str__(self):
        return self.value

@dataclass
class Human:
    name: str
    race: str
    country: str
    gender: Gender


human = Human(name='Gail Cliff', race='Black', country='KE', gender=Gender.MALE)
print(human.__str__())
print(human.name, human.race, human.country, human.gender)


def get_pows():
    for i in range(1, 10):
        yield i**i


foo = get_pows()
print(len(foo))
bar = [c for c in get_pows()]
print(bar)

next()