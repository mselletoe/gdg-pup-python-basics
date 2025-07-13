# Define the Car class
class Car:
    # The constructor method to initialize the object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to return a description of the car
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Create instances of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.describe())

# More test instances
car2 = Car("Ford", "Mustang", 1969)
print(car2.describe())

car3 = Car("Tesla", "Model S", 2023)
print(car3.describe())