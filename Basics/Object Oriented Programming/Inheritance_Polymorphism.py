# INHERITENCE

class Animal:

    def __init__(self):  # Constructor
        print("Animal Created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):  # Method overriding
        print("I am a Dog")

    def bark(self):
        print("Bow Bow")


my_animal = Animal()  # Constructor called
print my_animal.who_am_i()
print my_animal.eat()

my_dog = Dog()
print my_dog.who_am_i()  # Method called from Dog class, overiding happens
print my_dog.eat()  # Method called from Animal class, no overriding
print my_dog.bark()  # New method created in class Dog

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# POLYMORPHISM

class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


niko = Dog("Niko")
felix = Cat("Felix")

print niko.speak()
print felix.speak()

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak()) # pet.speak() does't know which speak() method we are calling, so objects makes a difference

pet_speak(niko) # same method names "speak()" but different objects (niko and felix)  --> Polymorphism
pet_speak(felix)