class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def fullName(self):
        return f"Brand:{self.__brand}, Model:{self.model}"

    def get_brand(self):
        return self.__brand


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


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.battery_size)
print(my_tesla.fullName())
print(my_tesla.get_brand())
