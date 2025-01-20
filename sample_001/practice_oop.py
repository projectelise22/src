# Classes
# think of a class as a blueprint for creating objects
# or a form/template for creating objects
# uses CamelCase for class names

class Dog:
    # class attributes
    species = "Canis familiaris"

    # constructor
    def __init__(self, name, age, coat_color):
        # instance attributes
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    # dunder method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # instance methods
    def speak(self, sound):
        return f"{self.name} says {sound}"

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")

class Car:
    # class attributes

    # constructor
    def __init__(self, color:str, mileage:int):
        self.color = color
        self.mileage = mileage
    
    # instance methods
    def description(self):
        print(f"The {self.color} car has {self.mileage} miles.")
    
    def drive(self, add_miles):
        self.mileage += add_miles
        print(self.mileage)

blueCar = Car("blue", 20_000)
blueCar.description()
redCar = Car("red", 30_000)
redCar.description()
newCar = Car("black", 0)
newCar.drive(5)
newCar.drive(100)

# OOP
# Inheritance - parent/child classes
# Extending - using super()
# Checking if it is an instance by isinstance(instance name, class name)

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

tucker = GoldenRetriever("Tucker", 2, "brown")
print(tucker.speak())

class Rectangle():

    # constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # descriptor
    def __str__(self):
        return f"This rectangle has a dimension of {length} x {width}"
    
    # instance methods
    def area(self):
        return (self.length * self.width)


class Square(Rectangle):
    def __init__(self, side_length):
        self.length = side_length
        self.width = side_length

square1 = Square(2)
print(square1.area())
square1 = Square(4)
print(square1.area())

# Challenge
class Animal():
    # class attributes
    location = "inside barn"
    animal_type = "not yet recognized"

    # constructor
    def __init__(self, name, number):
        self.name = name
        self.number += number

    # descriptor
    def __str__(self):
        return f"{number} of {animal_type}"
    
    # instance methods
    def speak(self, sound):
        return f"{name} is a {self.animal_type}"
    
    def walking(self):
        return is_walking == True
    
    def flying(self):
        return is_flying == True
    
    def running(self):
        return is_running == True
    
    def eating(self, food):
        return f"eating {food}"
    
    def produce(self, output):
        return output