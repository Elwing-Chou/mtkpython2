class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return (str(self.name) + "\t" +
                str(self.height) + "\t" +
                str(self.weight))

    def __repr__(self):
        return self.name

class SuperPerson(Person):

    def __init__(self, name, height, weight, city):
        Person.__init__(self, name, height, weight)
        self.city = city

    def __str__(self):
        return (str(self.name) + "\t" +
                str(self.height) + "\t" +
                str(self.weight) + "\t" +
                str(self.city))

p1 = SuperPerson("Elwing", 175, 75, "Taipei")
print(p1)
print(p1.calculate_bmi())
print([p1])