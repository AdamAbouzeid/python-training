import abc

# Inheritance
class Cat:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Cat's name: {self.name}")

class Tabby(Cat):
    def sound(self):
        print("Meow!")

cat = Tabby("Chipsy")
cat.display_name()
cat.sound()

print("==================================")

# Polymorphism
class Calculator:
    def add(self, *args):
        return sum(args)
    def subtract(self, *args):
        return args[0] - args[1]

calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))
print(calc.subtract(1, 2, 3))

print("===================================")

# Encapsulation
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self._model = model
        self.__year = year

    def get_info(self):
        return f"Name: {self.name}, Model: {self._model}, Year: {self.__year}"

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 0:
            self.__year = year
        else:
            print("Year can't be negative")

car = Car("BMW", 1999, 2020)
print(car.name)
print(car._model)
print(car.get_year())
car.set_year(2025)
print(car.get_info())

print("===================================")

#Abstraction
class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def display_name(self):
        print(f"Dog's name: {self.name}")

class Labrador(Dog):
    def sound(self):
        print("Woof!")

class GoldenRetriever(Dog):
    def sound(self):
        print("Bark!")

dogs = [Labrador("Lucy"), GoldenRetriever("Chloe")]
for dog in dogs:
    dog.display_name()
    dog.sound()