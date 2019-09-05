class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return self.name + ":" + str(self.bmi())

class SuperPerson(Person):
    def __init__(self, name, height, weight, city):
        Person.__init__(self, name, height, weight)
        self.city = city

    def __str__(self):
        return (self.name + "(" +
                self.city + ")" + ":" +
                str(self.bmi()))


p1 = Person("Elwing", 175, 75)
print(p1.bmi())
# print(Person.bmi(p1))
print(p1)

p2 = SuperPerson("Bob", 180, 80, "Taipei")
print(p2)
