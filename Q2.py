# QUESTION 2.1

num = int(input("Enter a number: "))
square = num * num

if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")


# QUESTION 2.2

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome Numbers:")

for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(num)


# QUESTION 2.3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = 1

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("HCF:", hcf)
print("LCM:", lcm)


# QUESTION 2.4

correct_password = "python123"

for attempt in range(1, 4):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect Password")

        if attempt == 3:
            print("Account Blocked")
        else:
            print("Attempts Remaining:", 3 - attempt)


# QUESTION 2.5

# A. TRIANGLE PATTERN

n = 5

print("Triangle Pattern:")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# B. PYRAMID PATTERN

print("Pyramid Pattern:")

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


# C. DIAMOND PATTERN

print("Diamond Pattern:")

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)