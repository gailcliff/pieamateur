import json


class Person:

    def __init__(self, fname, lname, age, hobbies):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.hobbies = hobbies


json_file = open('dict.json', 'w')
person = Person("cliff", "gail", 21, ['coding', 'music', 'karaoke'])
json.dump(person.__dict__, json_file, indent=3)
json_str = json.dumps(person.__dict__, indent=10)

print(json_str)

json_from_str = json.loads(json_str)
print(json_from_str)

# json_dat = json.load(open("dict.json", 'r'))
# print(type(json_dat['hobbies']))
# print(json_dat)