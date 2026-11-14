# QUESTION 5.1

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    print("Factorial:", factorial(num))


# QUESTION 5.2

def natural_sum(n):
    if n == 0:
        return 0

    return n + natural_sum(n - 1)


num = int(input("Enter a number: "))

print("Sum:", natural_sum(num))


# QUESTION 5.3

def reverse_string(text):
    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))


# QUESTION 5.4

def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)


x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

if n < 0:
    if x == 0:
        print("Zero cannot have a negative exponent")
    else:
        print("Power:", 1 / power(x, -n))
else:
    print("Power:", power(x, n))
