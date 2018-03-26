from car import Car
from electric_car import ElectricCar

my_new_car = Car('阿尔法·罗密欧', 'gulia', 2017)

print(my_new_car.get_deacriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_deacriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
