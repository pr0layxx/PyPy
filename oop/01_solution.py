class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def fullName(self):
        return f"Brand:{self.__brand}, Model:{self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petrol or Diesel"


my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())
# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.battery_size)
# print(my_tesla.fullName())
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
print(Car.total_car)