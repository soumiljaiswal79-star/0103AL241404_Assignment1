# QUESTION 7.1

import math

num = 25

print("Square Root:", math.sqrt(num))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))

angle = 30
radian = math.radians(angle)

print("Sin 30:", math.sin(radian))
print("Cos 30:", math.cos(radian))
print("Tan 30:", math.tan(radian))


# QUESTION 7.2: 

import random
import string

# Generate OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Generate random password
characters = string.ascii_letters + string.digits

password = ""

for i in range(8):
    password += random.choice(characters)

print("Random Password:", password)

# Generate random list
numbers = []

for i in range(5):
    numbers.append(random.randint(1, 100))

print("Random Numbers:", numbers)


# QUESTION 7.3: 

import datetime

today = datetime.datetime.now()

print("Current Date:", today.date())
print("Current Time:", today.time())

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

birth_date = datetime.date(birth_year, birth_month, birth_day)
current_date = datetime.date.today()

age = current_date.year - birth_date.year

if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Your Age:", age)


# QUESTION 7.4

import math


def circle_area(radius):
    return math.pi * radius * radius

def circle_circumference(radius):
    return 2 * math.pi * radius


def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


r = 5
print("Circle Area:", circle_area(r))
print("Circle Circumference:", circle_circumference(r))

l = 10
b = 5

print("Rectangle Area:", rectangle_area(l, b))
print("Rectangle Perimeter:", rectangle_perimeter(l, b))