from fad.baz import chaz
from dataclasses import dataclass


class Dog(chaz.Animal):

    def __init__(self, name):
        super().__init__(name, "Dog")

    def eat(self):
        super().eat()
        print("Munch munch\n")

    def move(self):
        super().move()
        print("Sprint sprint\n")


animal = chaz.Animal("Whale", "Animalia")
animal.eat()
animal.move()
print(animal)

dog: chaz.Animal = Dog("Simba")
dog.eat()
dog.move()
print(dog)

print(isinstance(dog, chaz.Animal))
print(isinstance(animal, Dog))
print(issubclass(Dog, chaz.Animal))
print(issubclass(chaz.Animal, Dog))


class Person:

    def __init__(self):
        self.names = []
        self.idx = 0

    def add_name(self, name):
        self.names.append(name)

    def __iter__(self):  # to initialize the iterator, use __iter__ and just return the class itself
        return self

    def __next__(self):  # for __next__, return the next desired variable when the next. raise StopIteration exception to signify that iteration should stop
        if self.idx == len(self.names):
            self.idx = 0
            raise StopIteration

        self.idx += 1
        return self.names[self.idx - 1]

    def get_names(self):  # this is creating a generator. just use the 'yield' keyword instead of return
        for person_name in self.names:
            yield person_name


person = Person()
person.add_name("vaught")
person.add_name("liss")
person.add_name("papiyier")
person.add_name("denda")
person.add_name("oliec")


# utilizing an iterator
for name in iter(person):
    print(name * 2)

# trying with next
iteratr = iter(person)
print("next:", next(iteratr))
print("next:", next(iteratr))
print("next:", next(iteratr))

nm_list = list(iteratr)
print(nm_list)

# utilizing a generator
for name in person.get_names():
    print("nayme: ", name)


#  generator expression. prefer generator expressions to list comprehensions because they're more memory efficient.
name_list = (name.upper() for name in person.names)
for name in name_list:
    print(name)

print(list(person.get_names()))