
class Dog:  # Use CamelCasing for class convention
    species = "mammal"

    def __init__(self, breed, name, spots):   # Constructor
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):  # self refers to class instances/self is referring to class Dog
        print("Bow Bow, My name is {} and number is {}".format(self.name, number))


my_dog = Dog("Lab", "Sammy", True)  # Calling a constructor when instance is created

print my_dog.breed
print my_dog.name
print my_dog.spots
print my_dog.species
my_dog.bark(100)

print("********************************")

class Circle:

    pi = 3.14  # Class object attribute

    def __init__(self, radius = 1):  # Default value of radius is 1 if no value is given
        self.rad = radius  # 'rad' is a global variable
        self.area = radius*radius*self.pi

    def getCircumference(self):
        return 2*self.pi*self.rad

my_circle = Circle(30)  # Creating an instance of class Circle

print my_circle.pi
print my_circle.rad
print my_circle.getCircumference()
print my_circle.area

# rad, area are class instances
