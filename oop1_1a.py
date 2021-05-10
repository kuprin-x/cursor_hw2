class Animals:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} for food can kill.')
    def sleep(self):
        print(f'{self.name} wants to sleep')

class Bobcat(Animals):
    def silent(self):
        print(f'{self.name} is silent.')

class Lion(Animals):
    def king(self):
        print(f'{self.name} is the king of an animals.')

class Turtle(Animals):
    def slow(self):
        print(f'{self.name} is slow.')

class Pig(Animals):
    def dirty(self):
        print(f'{self.name} is a dirty animal.')

class Wolf(Animals):
    def alone(self):
        print(f'{self.name} is a lone animal.')

res_bob = Bobcat('Bobcat')
res_lio = Lion('Lion')
res_tur = Turtle('Turtle')
res_pig = Pig('Pig')
res_wolf = Wolf('Wolf')

res_bob.silent()
res_wolf.eat()
res_lio.king()
res_tur.slow()
res_pig.sleep()

print('|-----|-----|-----|-----|-----|')
res_animals = [res_bob, res_lio, res_tur, res_pig, res_wolf]

for i in res_animals:
    print(f'{i} - {isinstance(i, Animals)}')

print('|-----|-----|-----|-----|-----|')





class Human:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} eating.')

    def sleep(self):
        print(f'{self.name} sleeping.')

    def study(self):
        print(f'{self.name} studying.')

    def work(self):
        print(f'{self.name} working.')

class Centaur(Human, Animals):


    def animal_sleep(self):
        Animals.sleep(self)

    def human_sleep(self):
        Human.sleep(self)

result1a = Centaur('Сrocodile')

result1a.work()
result1a.study()
result1a.human_sleep()
result1a.animal_sleep()