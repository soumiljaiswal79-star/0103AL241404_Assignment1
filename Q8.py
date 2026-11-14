# QUESTION 8.1: 


class Vehicle:
    def vehicle_info(self):
        print("This is a Vehicle")


class Car(Vehicle):
    def car_info(self):
        print("This is a Car")


class ElectricCar(Car):
    def electric_info(self):
        print("This is an Electric Car")


obj = ElectricCar()

obj.vehicle_info()
obj.car_info()
obj.electric_info()


# QUESTION 8.2


class Teacher:
    def teaching(self):
        print("Professor teaches students")


class Researcher:
    def research(self):
        print("Professor conducts research")


class Professor(Teacher, Researcher):
    def details(self):
        print("This is a Professor")


obj = Professor()

obj.details()
obj.teaching()
obj.research()


# QUESTION 8.3


class Shape:
    def display(self):
        print("Calculating Area")


class Circle(Shape):
    def area(self, r):
        print("Circle Area:", 3.14 * r * r)


class Rectangle(Shape):
    def area(self, l, b):
        print("Rectangle Area:", l * b)


class Triangle(Shape):
    def area(self, b, h):
        print("Triangle Area:", 0.5 * b * h)


c = Circle()
c.display()
c.area(5)

r = Rectangle()
r.display()
r.area(10, 5)

t = Triangle()
t.display()
t.area(6, 4)


# QUESTION 8.4


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog Barks")


class Cat(Animal):
    def sound(self):
        print("Cat Meows")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()


# QUESTION 8.5


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag

        return Complex(r, i)

    def display(self):
        print(self.real, "+", self.imag, "i")


c1 = Complex(5, 3)
c2 = Complex(2, 4)

c3 = c1 + c2

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("Sum:")
c3.display()


# QUESTION 8.6

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def display_salary(self):
        print("Salary:", self.__salary)


emp = Employee(50000)

emp.display_salary()


# QUESTION 8.7

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw(self, entered_pin, amount):
        if entered_pin != self.__pin:
            print("Incorrect PIN")

        elif amount <= 0:
            print("Invalid Amount")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", self.__balance)


atm = ATM(1234, 10000)

pin = int(input("Enter ATM PIN: "))

atm.check_balance(pin)

amount = int(input("Enter withdrawal amount: "))

atm.withdraw(pin, amount)


# QUESTION 8.8

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name:", self.name)
        print("Health:", self.health)


class Warrior(Character):
    def attack(self):
        print(self.name, "attacks using a sword")


class Mage(Character):
    def attack(self):
        print(self.name, "attacks using magic")


class Archer(Character):
    def attack(self):
        print(self.name, "attacks using a bow")


w = Warrior("Thor", 100)
m = Mage("Merlin", 80)
a = Archer("Robin", 90)

w.display()
w.attack()

m.display()
m.attack()

a.display()
a.attack()