fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

#output = []
#for fruit in fruits:
#    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax.
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]

# uppercased_fruits=[]
# for fruit in fruits:
#     uppercased_fruits.append(fruit.upper())
# print(uppercased_fruits)


# Exercise 2 - create a variable named capitalized_fruits and
# use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# capitalized_fruits=[]
# templist=[]
# string_for_joining = ""

# for fruit in fruits: #create loop to filter through fruits
#     if fruit.count(" ") > 0: #check for any fruit with spaces
#         placeholder = fruit.split(" ") #create a temporary placeholder where fruit is spilt
#         for split in placeholder: #cycle through the words that split
#             templist.append(split.capitalize()) #capitalize all split words and save new version into templist
#         for temp in templist: #cycle through templist
#             if string_for_joining == "": # if string is empty add temp string with no space
#                 string_for_joining += temp
#             else:
#                 string_for_joining += " " + temp# else if string is not empty add a space before temp
#         capitalized_fruits.append(string_for_joining) # add new string to capitalize_fruits
#     else:
#         capitalized_fruits.append(fruit.capitalize())#if no spaces just capitalize fruit and add to main list

# print(capitalized_fruits)


# # Exercise 3 - Use a list comprehension to make a variable
# # named fruits_with_more_than_two_vowels.
# # Hint: You'll need a way to check if something is a vowel.

# fruits_with_more_than_two_vowels=[]
# for fruit in fruits:
#    if fruit.count("a")>=2 or fruit.count("e")>=2 or fruit.count("i")>=2 or fruit.count("o")>=2 or fruit.count("u")>=2:
#        fruits_with_more_than_two_vowels.append(fruit)
# print(fruits_with_more_than_two_vowels)


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# fruits_with_only_two_vowels=[]
# for fruit in fruits:
#    if fruit.count("a") + fruit.count("e") + fruit.count("i") +  fruit.count("o") + fruit.count("u")==2:
#        fruits_with_only_two_vowels.append(fruit)
# print(fruits_with_only_two_vowels)


# Exercise 5 - make a list that contains each fruit with more than 5 characters

# fruits_with_more_than_5_characters=[]

# for fruit in fruits:
#     if len(fruit) > 5:
#         fruits_with_more_than_5_characters.append(fruit)

# print(fruits_with_more_than_5_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# fruits_with_exactly_5_characters=[]

# for fruit in fruits:
#     if len(fruit) == 5:
#         fruits_with_exactly_5_characters.append(fruit)

# print(fruits_with_exactly_5_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# fruits_with_less_than_5_characters=[]
# for fruit in fruits:
#      if len(fruit) < 5:
#         fruits_with_less_than_5_characters.append(fruit)
# print(fruits_with_less_than_5_characters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# number_of_characters_in_each_fruit = []
# for fruit in fruits:
#     if fruit.count(" ") > 0:
#         number_of_characters_in_each_fruit.append(len(fruit)-fruit.count(" "))
#     else:
#         number_of_characters_in_each_fruit.append(len(fruit))

# print(number_of_characters_in_each_fruit)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# fruits_with_letter_a = []

# for fruit in fruits:
#     if fruit.count("a")>0:
#         fruits_with_letter_a.append(fruit)
# print(fruits_with_letter_a)


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# odd_numbers = []

# for number in numbers:
#     if number % 2 != 0:
#         odd_numbers.append(number)
# print(odd_numbers)


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# positive_numbers = []
# for number in numbers:
#     if number > 0:
#         positive_numbers.append(number)
# print(positive_numbers)


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# negative_numbers = []
# for number in numbers:
#     if number < 0:
#         negative_numbers.append(number)
# print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals



# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.