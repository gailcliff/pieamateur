# import app
from app import test, Test
from enum import Enum
import sys
import bisect


@test('/cliff')
def foo():
    return "bar"


if __name__ == '__main__':
    print(foo)

    test = Test('grep')
    print(test.test_name)


    class Person:
        token: str
        __persons__: list = []

        def __init__(self, name: str):
            self.name = name

        def add_to_roster(self):
            self.__persons__.append(self)

        def __str__(self):
            return self.name

        @classmethod
        def roster(cls):
            for person in cls.__persons__:
                yield person


    class Level(Enum):
        FRESHMAN = 'frosh'
        SOPHOMORE = 'soph'
        JUNIOR = 'jr'
        SENIOR = 'sr'


    class Student(Person):
        avg = 70
        score: int
        level: Level

        def __init__(self, name: str, level: Level, score: int):
            super().__init__(name)
            self.level = level
            self.score = score

        @classmethod
        def increase_avg(cls):
            cls.avg += 1
            cls.level = Level.SENIOR

        @classmethod
        def sort_key(cls, student):
            return -student.score

        def add_to_roster(self):
            bisect.insort(Person.__persons__, self, key=Student.sort_key)

        def print_avg(self):
            print(self.avg)

        def pass_level(self):
            print(f"passed {self.level.name} with gpa > 2.0")

        def __str__(self):
            return super().__str__() + ": " + str(self.score)


    class PersonIter:
        persons: list[Person]
        curr_idx: int

        def __init__(self, persons):
            self.curr_idx = 0
            self.persons = persons

        def __iter__(self):
            return self

        def __len__(self):
            return len(self.persons)

        def __next__(self):
            if self.curr_idx == len(self.persons):
                raise StopIteration
            person = self.persons[self.curr_idx]
            self.curr_idx += 1
            return person


    args = sys.argv
    # student = Student(args[1], Level(args[2]))
    # student1 = Student(args[1], Level(args[2]))
    # print(student)
    # student.pass_level()
    #
    # print(isinstance(student, Person))
    # print(isinstance(student, Student))
    # print(issubclass(Student, Person))
    # print(issubclass(Person, Student))
    #
    # Student.increase_avg()
    # student.print_avg()
    #
    # Student.increase_avg()
    # student1.print_avg()

    # Student.increase_avg()
    # student.print_avg()
    #
    # Student.increase_avg()
    # student1.print_avg()
    # print(student1.level)

    while True:
        token = input("Enter student name and score: ")

        if token == '!':
            roster_iter = iter(PersonIter(list(Person.roster())))

            from pprint import pprint
            pprint([str(p) for p in roster_iter])
            break

        token = token.split()

        student = Student(token[0], Level(token[1]), int(token[2]))
        student.add_to_roster()


