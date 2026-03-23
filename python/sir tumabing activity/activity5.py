# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def role_duty(self):
        print(f"{self.name} is living life.")

# Child Classes

class Worker(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def role_duty(self):
        print(f"{self.name} works as a {self.job} to earn money.")

class Parent(Person):
    def __init__(self, name, age, child_count):
        super().__init__(name, age)
        self.child_count = child_count

    def role_duty(self):
        print(f"{self.name} takes care of {self.child_count} children.")

class Player(Person):
    def __init__(self, name, age, game):
        super().__init__(name, age)
        self.game = game

    def role_duty(self):
        print(f"{self.name} plays {self.game}.")

class ChurchServant(Person):
    def __init__(self, name, age, ministry):
        super().__init__(name, age)
        self.ministry = ministry

    def role_duty(self):
        print(f"{self.name} serves in the {self.ministry} ministry.")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def role_duty(self):
        print(f"{self.name} studies {self.course}.")


people = [
    Worker("John", 30, "Engineer"),
    Parent("Maria", 40, 3),
    Player("Alex", 20, "Basketball"),
    ChurchServant("Liza", 28, "Music"),
    Student("Rainer", 19, "IT")
]

for person in people:
    person.role_duty()
