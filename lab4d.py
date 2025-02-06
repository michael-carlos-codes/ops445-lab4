#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    return string[:5]

def last_seven(string):
    return string[-7:]

def middle_number(number):
    number_str = str(number)
    return number_str[1:3]  # Returns second and third character

def first_three_last_three(string1, string2):
    return string1[:3] + string2[-3:]

if __name__ == '__main__':
    print(first_five(str1))  # Should print 'Hello'
    print(first_five(str2))  # Should print 'Senec'
    print(last_seven(str1))  # Should print 'World!!'
    print(last_seven(str2))  # Should print 'College'
    print(middle_number(num1))  # Should print '50'
    print(middle_number(num2))  # Should print '.5'
    print(first_three_last_three(str1, str2))  # Should print 'Helege'
    print(first_three_last_three(str2, str1))  # Should print 'Send!!'


# lab4d.py
text = 'Seneca'
letter = text[1]
print(letter)

# Step 2: Loop through the string and print each character with its index
offset = 0
length = len(text)
while offset < length:
    print(offset, text[offset])  # Prints index and character
    offset = offset + 1

# Step 3: Use a for loop to iterate through the string
for letter in text:
    print(letter)  # Prints each character of the string

# Step 4: Create a function to search for a specific character
def find(text, char):
    for letter in text:
        if letter == char:
            return True
    return False

# Test the find function
if __name__ == '__main__':
    s1 = 'Seneca'
    print(s1, 'contains letter s? ->', find(s1, 's'))
    print(s1, 'contains letter S? ->', find(s1, 'S'))

# Step 5: Replace the find function with 'in' operator
s1 = 'Seneca'
print(s1, 'contains letter s? ->', 's' in s1)
print(s1, 'contains letter S? ->', 'S' in s1)

# Step 6: Count vowels in the string
def is_vowel(char):
    if char in 'aeiou':
        return True
    return False

if __name__ == '__main__':
    text = 'Seneca'
    vowel_count = 0
    for char in text:
        if is_vowel(char):
            vowel_count += 1
    print('There are', vowel_count, 'vowel(s) in', text)
