name = input('What is your name? ')
print('Hello ' + name)

name = 'Jamila'
age = 18
pi = 3.14
cars = ['bmw', 'mercedes', 'range rover', 'toyota', 'honda']
print(name)
print(age)
print(pi)
print(cars)

first_name = 'jamila'
surname = 'Smith'
full_name = first_name.capitalize() + ' ' + surname
print(full_name)
print(len(first_name))
print(len(surname))
print(full_name.endswith('Smith'))

addition = 10 + 5
print(addition)
subtraction = 10 - 5
multiplication = 10 * 5
division = 10 / 5
print(subtraction)
print(multiplication)
print(division)
mod = 10 % 4
print(mod)

print(10 < 10)
is_adult = False
is_teenager = False

if is_adult:
    print("is adult")

age = 15
if age >= 18:
    print('adult')
else:
    print('not an adult')

print(len(cars))
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])

print('LOOP CARS')
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())


number = 0
while number <= 10:
    print(number)
    number = number + 1
else:
    print('while loop ended and value of number is ' + str(number))


age = 18
age2 = 17

def check_age(age):
    print('check age function was invoked')
    if age < 18:
        print('ooops not an adult')
    else:
        print('hooray I am an adult')

check_age(age)
check_age(age2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking...')
    
    def speak(self):
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old')

john = Person('John', 22)
mariam = Person('Mariam', 18)

print(john.name + ' ' + str(john.age))
john.speak()
john.walk()
print(mariam.name + ' ' + str(mariam.age))
mariam.speak()
mariam.walk()