# QUESTION 1.1

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10

if bill > 2000:
    bill = bill + bill * 0.05

print("Total Electricity Bill: Rs.", bill)


# QUESTION 1.2

salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))
age = int(input("Enter age: "))

count = 0

if salary >= 30000:
    count += 1

if credit >= 700:
    count += 1

if 21 <= age <= 60:
    count += 1

if count == 3:
    print("Loan Approved")
elif count == 2:
    print("Conditionally Approved")
else:
    print("Loan Rejected")


# QUESTION 1.3

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# QUESTION 1.4

marks = []

for i in range(5):
    m = int(input("Enter marks of subject " + str(i + 1) + ": "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if any(m < 33 for m in marks):
    print("Result: Fail")
elif percentage >= 60:
    print("First Division")
elif percentage >= 50:
    print("Second Division")
elif percentage >= 40:
    print("Third Division")
else:
    print("Fail")
