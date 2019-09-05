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

p1 = Person("Elwing", 175, 75)
# print(a) -> str(a) -> a.__str__
print(p1)
print([p1])
print(p1.calculate_bmi())
b = Person
p2 = b("Bob", 180, 80)
print(p2.calculate_bmi())