from copy import deepcopy

class Animal:
    number_of_animals = 0
    def __init__(self, latin_name, birth_age, weigth, location):
        self.latin_name = latin_name
        self.birth_age = birth_age
        self.weight = weigth
        self._location = location
        Animal.number_of_animals ++ 1

    def say_hello(self):
        print(f'Hello, I am {self.latin_name} {self.birth_age} {self.weight}')
    
    def __repr__(self):
        return f'{self.latin_name}'
    
    def say_your_age(self, now_year):
        print('Hello, I am ', now_year - self.birth_age, 'years old')
    

animal_1 = Animal('Loren ipsum', 2019, 5, 350)

#animal_1.say_hello()

#print(animal_1)
animal_1.say_your_age(2020)

animal_2 = deepcopy(animal_1)

animal_2.latin_name = 'Ipsim lorem'

print(animal_1)
print(animal_2)


class Dog(Animal):

    def say_hello(self):
        print('Av av av av')

rex = Dog('Camus', 2019,5,200)

print(rex)