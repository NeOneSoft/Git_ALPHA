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

<<<<<<< HEAD
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

def names(names_list):
    for name in names_list:
        print(name)
        
names(names_list = ['Pedro', 'Hugo', 'Paco', 'Luis'])
=======
class Person:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

class Man(Person):
    def working(self):
        print("I'm Working")
>>>>>>> 147efb7 (add Man Class inherit Person)
