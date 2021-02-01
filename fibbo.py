def fibbo_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield "{}:{}".format(i + 1, a)
        a, b = b, a + b

for item in fibbo_generator(10):
    print(item)

def users():
    users = dict(first_name = "Gonzalo", 
                last_namem = "Romero",
                gender = "M",
                age = 36
                )
    users['profession'] = "Software Enginner" 
    print(users)

users()

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Sport(Car):
    def turn_On(self):
        print("This car is On")

    def turn_Off(self):
        print("This car is Off")

my_car = Sport('Mini', 'Jhon Cooper', '2021')
print(my_car.brand, my_car.model, my_car.year)
my_car.turn_On()
my_car.turn_Off()


def fizz_buzz(n):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Fizz")
    elif n % 3 == 0:
        print("Buzz")

fizz_buzz(25)