# QUESTION 4.1

numbers = [1, 2, 3, 4, 5]

k = int(input("Enter rotation positions: "))
direction = input("Enter direction (left/right): ").lower()

k = k % len(numbers)

if direction == "left":
    result = numbers[k:] + numbers[:k]
elif direction == "right":
    result = numbers[-k:] + numbers[:-k] if k != 0 else numbers
else:
    result = numbers

print("Original List:", numbers)
print("Rotated List:", result)


# QUESTION 4.2

numbers = [1, 2, 3, 2, 4, 1, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Original List:", numbers)
print("List without duplicates:", result)


# QUESTION 4.3

numbers = [1, 2, 3, 5, 6]

n = 6

total = n * (n + 1) // 2
missing = total - sum(numbers)

print("Missing Number:", missing)


# QUESTION 4.4

subjects = ("Python", "Java", "DBMS", "OS", "Deep Learning")

print("Third Subject:", subjects[2])
print("Total Subjects:", len(subjects))
print("Index of DBMS:", subjects.index("DBMS"))


# QUESTION 4.5

data = ((1, "A"), (2, "B"))

result = dict(data)

print("Dictionary:", result)


# QUESTION 4.6

t = (10, 20, 30, 40, 50)

first, *middle, last = t

new_tuple = (last, *middle, first)

print("Original Tuple:", t)
print("After Swapping:", new_tuple)


# QUESTION 4.7

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("Set1 is a Subset of Set2")
else:
    print("Set1 is Not a Subset of Set2")


# QUESTION 4.8

students = [
    ("Aman", 85),
    ("Rahul", 28),
    ("Priya", 92),
    ("Neha", 65),
    ("Rohit", 30)
]

highest = 0
topper = ""
total = 0
failed = []

for name, marks in students:
    total += marks

    if marks > highest:
        highest = marks
        topper = name

    if marks < 33:
        failed.append(name)

average = total / len(students)

print("Topper:", topper)
print("Highest Marks:", highest)
print("Average Marks:", average)
print("Failed Students:", failed)




# QUESTION 4.9

library = {
    "Python": 5,
    "Java": 3,
    "C++": 4
}

print("Library Books:", library)

library["DBMS"] = 6
library["Python"] = 7

book = input("Enter book name to search: ")

if book in library:
    print("Book Available")
    print("Quantity:", library[book])
else:
    print("Book Not Available")

print("Updated Library:")

for name, quantity in library.items():
    print(name, ":", quantity)