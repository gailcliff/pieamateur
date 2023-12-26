from dataclasses import dataclass

from spin4 import Animal


animal = Animal()
print(animal.name)
print(animal.age)
print(animal._species)

animal.name = 'mania'
animal.age += 1
animal._species.append("birds")
print(animal.name)
print(animal.age)
print(animal._species)

animal2 = Animal()
print("Animal 2:", animal2.name, ",", animal2.age, animal2._species)


@dataclass
class Species:
    name: str
    scientific_name: str


species1 = Species("human beings", "Homo sapiens")
species2 = Species("tilapia", "Oreochromis niloticus")
species3 = Species("tilapia", "Gallus gallus")

print(species2)
print(species3.name)
print(species1.scientific_name)


gen = (i**2 for i in range(1,10))
geni = iter(gen)

print(next(geni))
print(next(geni))

for j in geni:
    print(j, end=' ')

print()

print(list(gen))