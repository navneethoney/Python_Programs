
from collections import namedtuple

Dog = namedtuple('Dog', 'name age breed')  # 'Dog' is the object type
sam = Dog(name = "Sammy", age = 2, breed = "Lab")

print(sam)
print(sam.age)
print(sam.name)
print(sam.breed)

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur = "fuzzy", claws = False, name = "kitty")

print(c[0])  # It can be treated as a normal tuple also
print(c.fur)