# The number inside the [] is called "INDEX"
# Index should be just INTEGERS

# Exercise 1: How to see the 0 and the first letters of the variable "fruit"?
fruit = 'banana'

letter0 = fruit[0]
letter1 = fruit[1]
print(letter0)
print(letter1)
print(len(fruit))

# Exercise 2: How to see the last letter of the variable "fruit"?
# Option 1:
length = len(fruit)
last = fruit[length-1]
print(last)
# Option 2:
print(fruit[-1])

# Exercise 3: How to see al the letter from the variable "fruit"?
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# Exercise 4: How to see the variable "fruit" in a contrary order?
#index = 5
#while index < len(fruit):
    #letter = fruit[index]
    #print(letter)
    #index = index - 1

# Exercise 5: How to see all letters from a variable s = 'Monty Python' with the separated words?
s = 'Monty Python'
# Option 1:
print(s[0:5])
print(s[6:12])
# Option 2:
print(s[:5])
print(s[6:])

# Exercise 6: Write all the variable "fruit"
# Option 1:
print(fruit[:])
# Option 2:
print(fruit)

# Exercise 7: How to change a string? - Change the first letter and concatenate the words
string = 'Hello world!'
new_string = 'J' + string[1:]
print(string)
print(new_string)

# Exercise 8: How to count the letters of a word?
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Exercise 9: How to know if a word comes before or after another word?
# Reminder: Python does not handle uppercase and lowercase letters the same way that people do.
# All the uppercase letters come before all the lowercase letters, for example:
# Your word, Pineapple, comes before banana.
#word = input('Write the name of a fruit: ')
word = 'banana'
lower_word = word.lower()
if lower_word < 'banana':
    print('Your word, ' + lower_word + ', comes before banana.')
elif lower_word > 'banana':
    print('Your word, ' + lower_word + ', comes after banana.')
else:
    print('All right, bananas.')

# Exercise 10: How to know the type and the method (function) of an object in Python?
# Reminder 1: Method and function are similar, the difference is in their syntax
# Reminder 2: The order of the syntax is string.method(), ex: stuff.upper()
#stuff = input('Write whatever you want: ')
#print(type(stuff))
#print(dir(stuff))

# Exercise 11: Use and explain each method that Python has for each string written by an user
word = input('Write whatever you want: ')

# Method 1 --> capitalize: Capitalize the first letter of a word or a phrase
print(word.capitalize())

# Method 2 --> center: Centralize a word or a phrase
# Reminder: 2 arguments --> center(width, 'something') --> width could be a float or ab integer, 'something' is a str
print(word.center(40, ' '))
print(word.center(10, ' '))

# Method 3 --> count: Count the number of a letter or of a word or even a phrase in a text
# Reminder: It takes 3 arguments --> count('str', number, number) --> 'str' is the letter or word or even phrase that we
# want to search. 'start' is the first position of the text that we want to search.
# 'end' is the last position of the text that we want to search
# Ex: count('i', 0, 10) --> We want to search the letter "i" being the first position to search the character number "0"
# and the last one the character number "10"
# By default Python will search between the first and the last character written
print('There are', word.count('i'), '"i" in the text')

# Method 4 --> How to encode a text to UTF-8? - By default Python encode to UTF-8
print(word.encode)

# Method 5 --> How to search for suffixes in a text?
text = input('The events are coming...')
print('The first word is', text.endswith('the', 0, 10))

# Method 6 --> How to tab a word or a number in order to create columns?
# Reminder: .expandtabs(integer) By default is 8
# Examples:
# When you set the tabsize to 2: The tab stops are 2, 4, 6, 8 and so on.
# When you set the tabsize to 3: The tab stops are 3, 6, 9 and so on.
# When you set the tabsize to 4. The tab stops are 4, 8, 12 and so on.
# When you set the tabsize to 5. The tab stops are 5, 10, 15 and so on.
# When you set the tabsize to 6. The tab stops are 6, 12, 18 and so on.
number1 = '1\t12\t123\t1234\t12345'.expandtabs(8)
print(number1)

number2 = '1\t12\t123\t1234\t12345'.expandtabs(2)
print(number2)

number3 = '1\t12\t123\t1234\t12345'.expandtabs(3)
print(number3)

number4 = '1\t12\t123\t1234\t12345'.expandtabs(4)
print(number4)

number5 = '1\t12\t123\t1234\t12345'.expandtabs(5)
print(number5)

number6 = '1\t12\t123\t1234\t12345'.expandtabs(6)
print(number6)
