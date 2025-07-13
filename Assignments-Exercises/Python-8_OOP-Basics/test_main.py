# create class
class Car:
    
    #constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."


# create instances
car1 = Car("Toyota", "Corolla", 2020)
print(car1.describe())

car2 = Car("Honda", "Civic", 2022)
print(car2.describe())

car3 = Car("Tesla", "Model 3", 2023)
print(car3.describe())