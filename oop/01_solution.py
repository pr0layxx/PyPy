class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Brand:{self.brand}, Model:{self.model}"


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())
my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
