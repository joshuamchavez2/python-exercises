# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

# day_of_the_week = input("Enter a day of the week>\n") # prompt the user for a day of the week
# if day_of_the_week.lower() == "monday": # print out whether the day is Monday or not
#     print("You typed Monday!")
# else:
#     print(f"You did not type Monday....the best day of the week. So sad...{day_of_the_week} is not as cool")

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# weekday_or_weekend = input("Enter a day of the week>\n")
# weekday =["monday", "tuesday", "wednesday", "thursday", "friday"]
# weekend =["saturday", "sunday"]

# if weekday_or_weekend.lower() in weekday:
#     print(f"{weekday_or_weekend} is a weekday")
# elif weekday_or_weekend.lower() in weekend:
#     print(f"{weekday_or_weekend} is a weekend")
# else:
#     print("You did not type a day of the week.")


# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours


# hours_worked_in_week = 41
# hourly_rate = 39

# def weekly_paycheck(hours_worked_in_week, hourly_rate):
#     if(hours_worked_in_week > 40):
#         return print(hours_worked_in_week * hourly_rate * 1.5)
#     else:
#         return print(hours_worked_in_week * hourly_rate)

# weekly_paycheck(hours_worked_in_week, hourly_rate)


# Loop Basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

# i = 5
# while(i <= 15):
#     print(i)
#     i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each
# number with a new line.

# i=0
# while i <=100:
#     print(i)
#     i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

# i = 100
# while i >= -10:
#     print(i)
#     i-=5

# Create a while loop that starts at 2, and displays the number squared on each line while the number
# is less than 1,000,000.

# i=2
# while i <= 1000000:
#     print(i)
#     i **= 2

# Write a loop that uses print to create the output shown below.

# i=100
# while i >= 5:
#     print(i)
#     i -= 5

# For Loops

# Write some code that prompts the user for a number,
#then shows a multiplication table up through 10 for that number.

# number = input("Select a number>")
# if number.isdigit():
#     i=1
#     while i<=10:
#         print(f"{number} x {i} = {int(number) * i}")
#         i+=1
# else:
#     print("you did not enter a number.")

# Create a for loop that uses print to create the output shown below.

# i=1
# for i in range(1, 10):
#     print(str(i)* i)

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

number_to_skip = input("Select an odd number between 1 and 50>")

number = 1 
while number <=50:
    if number == int(number_to_skip):
        print(f"Yikes! Skipping number: {number_to_skip}")
    else:
        print(f"Here is an odd number: {number}")
    number +=2 

# Your output should look like this:


# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49
# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125
# Bonus: Research python's format string specifiers to align the table

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.