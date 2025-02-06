#!/usr/bin/env python3

def join_sets(s1, s2):
    return s1 | s2

def match_sets(s1, s2):
    return s1 & s2

def diff_sets(s1, s2):
    return s1 ^ s2

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))


course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445

print(course_name)
print(course_code)
print(str(course_number))
print(course_name + ' ' + course_code + ' ' + str(course_number))

print('Line 1\nLine 2\nLine 3\n')
print(course_name.lower())         # Converts to lowercase
print(course_name.upper())         # Converts to uppercase
print(course_name.swapcase())      # Swaps case
print(course_name.title())         # Title case (first letter of each word uppercase)
print(course_name.capitalize())

lower_name = course_name.lower()
print(lower_name)
list_of_strings = lower_name.split(' ')
print(list_of_strings)
print(list_of_strings[0])  # First element

print(list_of_strings[0].upper())  # Uppercase the first word

print(course_code[0])      # First character
print(course_code[2])      # Third character
print(course_code[-1])     # Last character

print(course_name[0:4])    # First four characters
print(course_code[0:3])    # First three characters
print(course_name[12:])    # Substring from index 12 to end

print(course_name[-1])     # Last character
print(course_name[-2])     # Second last character

print(course_name[0:4] + course_name[-10:-6])  # Combine two substrings
substring = course_name[0:4] + course_name[-10:-6]
print(substring)

