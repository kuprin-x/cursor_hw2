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

result1 = Bobcat('Bobcat')
result1.sleep()
result1.eat()
result1.silent()



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