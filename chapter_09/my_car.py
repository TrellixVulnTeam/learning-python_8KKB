from car import Car

my_new_car = Car('阿尔法·罗密欧', 'gulia', 2017)
print(my_new_car.get_deacriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
