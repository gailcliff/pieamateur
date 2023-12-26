def loo():
    print("poop")


class Animal:

    name: str
    species: str

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._sound = 'awoo'

    def eat(self):
        print(self.name, " eating")

    def move(self):
        print(self.name, " moving")

    def __str__(self):
        return f"{self.name} of the species {self.species}"

