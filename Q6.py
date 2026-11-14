# QUESTION 6.1

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("You are Eligible")

except ValueError as e:
    print("Error:", e)


# QUESTION 6.2

balance = 10000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance")

    if amount <= 0:
        raise ValueError("Enter a valid withdrawal amount")

    balance -= amount

    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

except ValueError as e:
    print("Error:", e)


# QUESTION 6.3

class PasswordError(Exception):
    pass


password = input("Enter your password: ")

try:
    if len(password) < 8:
        raise PasswordError("Password must contain at least 8 characters")

    if not any(ch.isupper() for ch in password):
        raise PasswordError("Password must contain an uppercase letter")

    if not any(ch.isdigit() for ch in password):
        raise PasswordError("Password must contain a number")

    print("Password is Valid")

except PasswordError as e:
    print("Invalid Password:", e)
