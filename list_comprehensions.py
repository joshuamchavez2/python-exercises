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

capitalized_fruits=[]

for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())
    if fruit.count(" ") > 0:
        templist = fruit.split(" ")
        for temp in templist:
        print(templist)


print(capitalized_fruits)


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.