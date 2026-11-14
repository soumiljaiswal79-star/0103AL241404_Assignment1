# QUESTION 3.1

text = input("Enter a string: ")

text = text.replace(" ", "").lower()

if text == text[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")


# QUESTION 3.2

sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)
print("Length:", len(longest))


# QUESTION 3.3

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")


# QUESTION 3.4

text = input("Enter a string: ")

result = ""

for char in text:
    if char not in result:
        result += char

print("String after removing duplicates:", result)


# QUESTION 3.5

text = input("Enter a string: ")

result = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1

print("Compressed String:", result)