# Define a function named is_two. It should accept one input and return
# True if the passed input is either the number or the string 2, False otherwise.


def is_two(input_value):
    '''using an if statement to check if the input was either a string or
    integar type'''
    if type(input_value) == int or type(input_value) == str:
        return True
    else:
        return False

print(is_two([1, 2, 3]))
print(is_two(1))
print(is_two("abc"))


'''Define a function named is_vowel. It should return True if the passed string
    is a vowel, False otherwise.'''
def is_vowel(input_value):
    '''using an if statement to check if the input is a vowel, aeiou.'''
    if input_value in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False
    
print(is_vowel("a"))
print(is_vowel("i"))

# Define a function named is_consonant. It should return True if the passed
# string is a consonant, False otherwise. Use your is_vowel function to
# accomplish this.

def is_consonant(input_value):
    '''used an if statement and my last function to check if its not a vowel.'''
    if is_vowel(input_value)==True:
        return False
    else:
        return True

print(is_consonant("a"))
print(is_consonant("b"))
print(is_consonant("c"))
print(is_consonant("d"))  
print(is_consonant("e"))
print(is_consonant("f"))     
    

# Define a function that accepts a string that is a word. The function should
# capitalize the first letter of the word if the word starts with a consonant.

def cap_1st_letter_if_consonant(input_value):
    '''if statement is checking if the first value in the input is a vowel.'''
    if is_consonant(input_value[0]) == True:
        '''if so, return that input but capitalized.'''
        return input_value.capitalize()
    else:
        return input_value

print(cap_1st_letter_if_consonant("bbcd"))

# Define a function named calculate_tip. It should accept a tip percentage
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    '''converting percent to decimal then adding one to number. This way I only 
    have to multiply values together to get the right value.''' 
    tip_percentage = (tip_percentage / 100) + 1
    return bill_total * tip_percentage

print(calculate_tip(10, 100))
print(calculate_tip(10, 200))
print(calculate_tip(10, 300))
print(calculate_tip(10, 15))

# Define a function named apply_discount. It should accept a original price,
# and a discount percentage, and return the price after the discount is
# applied.

def apply_discount(discount_percentage, original_price):
    '''doing the same as above only subtracting the decimal from 1 instead of
    adding 1.  Again this makes multiplying easier.'''
    discount_percentage = 1 - (discount_percentage/100)
    return original_price * discount_percentage    

print(apply_discount(10, 100))


# Define a function named handle_commas. It should accept a string that is a
# number that contains commas in it as input, and return a number as output.

def handle_commas(input_value):
    '''Created a list called placeholder and im just using it to hold data'''
    placeholder = []
    '''value_with_no_commas will be my return value.  Declaring it empty.''' 
    value_with_no_commas = ""
    '''checking to see if there are any commas in the input'''
    if "," in input_value:
        '''if there is a comma, split the values into a the temp list using
        commas as the splitting points'''
        placeholder = input_value.split(",")
        '''loop through the list and join each char to value w/no commas.'''
        for place in placeholder:
             value_with_no_commas = ''.join(placeholder)
        return value_with_no_commas
    
print(handle_commas("1,000"))
print(handle_commas("1,000,000,000"))

# Define a function named get_letter_grade. It should accept a number and
# return the letter grade associated with that number (A-F).


def get_letter_grade(grade):
    '''using if statements and range to return the appropriate grade.'''
    if grade in range(99,101):
        return "A+"
    elif grade in range(93,99):
        return "A"
    elif grade in range(90,93):
        return "A-"

    elif grade in range(88,90):
        return "B+"
    elif grade in range (83, 88):
        return "B"
    elif grade in range(80,83):
        return "B-"

    elif grade in range(78,80):
        return "C+"
    elif grade in range (73, 78):
        return "C"
    elif grade in range(70,73):
        return "C-"

    elif grade in range(68,70):
        return "D+"
    elif grade in range (63, 68):
        return "D"
    elif grade in range(60,63):
        return "D-"

    elif grade in range(58,60):
        return "F+"
    elif grade in range (50, 58):
        return "F"
    elif grade in range(0,50):
        return "F-"
    else:
        print("Please enter a valid numerical grade ranging from 0-100")

print(get_letter_grade(100))
print(get_letter_grade(88))
print(get_letter_grade(65))
print(get_letter_grade(92))
print(get_letter_grade(42))


# Define a function named remove_vowels that accepts a string and returns a
# string with all the vowels removed.

def remove_vowels(input_value):
    '''using the same variables as placeholder/return value as two problems 
    above'''
    placeholder = []
    removed_vowels_from_input = ""
    for value in input_value:
        '''using a loop and if statement to find if the current value is a vowel
        using my is_vowel function defined above.'''
        if is_vowel(value)!=True:
            '''if it is not a vowel save the char into placeholder'''
            placeholder.append(value)
    '''join all the chars in place holder into removed_vowels variable.'''
    removed_vowels_from_input = "".join(placeholder)
    return removed_vowels_from_input
            

print(remove_vowels("hello"))
print(remove_vowels("abcdefghijklmnopqrstuvwxyz"))


# Define a function named normalize_name. It should accept a string and
# return a valid python identifier, that is:

def leading_spaces(input_value):
    '''cleaned_string is currently a declared empty string.  it will eventually
    be my return value.'''
    cleaned_string = ""
    
    '''I am enumerating through input_value to find the first leading
    none space " " char'''
    for index, value in enumerate(input_value):
        if value != " ":
            '''once i find the first none space char, i am taking that index of
            that no space char and start to rebuild the original string
            starting at that index.  which will remove any leading spaces.'''
            for i in range(index, len(input_value)):
                cleaned_string += input_value[i]
            '''after my string it built there is no need to continue the loop
            as the starting index was already found so i break out of it.''' 
            break
        
    return cleaned_string

def reversed_string(input_value):
    '''This method just returns a string in reverse order.'''
    reversed_string = ""
    for value in reversed(input_value):
        reversed_string += value
    return reversed_string

def trailing_spaces(input_value):

    flipped_string = ""
    cleaned_string = ""
    
    '''since I already defined a function that removes leading spaces. If a 
    string were to have trailing spaces, i could just reverse the string and
    feed it back to my leading_spaces function to take care of those too'''
    flipped_string = reversed_string(input_value)
    flipped_string = leading_spaces(flipped_string)
    
    '''once the flip and cleaning is done, its time to flip it back without the
    trailing spaces.'''
    cleaned_string = reversed_string(flipped_string)
    return cleaned_string


def number_as_start(input_value):
    '''this function is the same as the empty spaces, instead it's looking for 
    more than just a space as a first char but any numeric that is the first
    char'''
    cleaned_string = ""

    for index, value in enumerate(input_value):
        if value not in "123456790":
            for i in range(index, len(input_value)):
                cleaned_string += input_value[i]
            '''once i have found my index of the first none numeric char I will
            build my string and break the loop'''
            break
                
        
    return cleaned_string

def replace_spaces_with_underscore(input_value):
    '''this function will just replace any char that is a space with an under
    score'''
    cleaned_string = ""
    for value in input_value:
        if value == " ":
            cleaned_string += "_"
        else:
            cleaned_string += value
            
    return cleaned_string

def special_symbos(input_value):
    '''this function will just remove any special char and rebuild the string
    score'''
    cleaned_string = ""

    for value in input_value:
        if value not in "~!@#$%^&*()+=-,.<>/?\|~;:[]{}":
            cleaned_string += value
    return cleaned_string

def string_to_lower_case(input_value):
    '''this function will turn all char in lower case'''
    return input_value.lower()

def normalize_name(input_value):
    '''this is function that ties all the above functions together'''

    while input_value[0] in "0123456789 " or input_value[len(input_value)-1] in " ":
        '''this while loop is here just in case we removed all leading spaces
        or numbers once but the next leading chars were also problems. 
        Basically, this while loop will keep cleaning until there is no
        trailing/leading spaces or trailing numbers'''
        input_value = leading_spaces(input_value)
        input_value = trailing_spaces(input_value)
        input_value = number_as_start(input_value)
        input_value = special_symbos(input_value) 
       
    input_value = replace_spaces_with_underscore(input_value)
    input_value = string_to_lower_case(input_value)
    return input_value

test_code = "1 2 3 $()&^$( T#%^H#%^i%^s%^ i%^&S %&(*(a v$%&AlI#%^d p#%^YTh#%^on id#%^%&en$%&TI#$^%%$&^*Fi@$%^*(er  #^#^#@"

print(normalize_name(test_code))

# Write a function named cumulative_sum that accepts a list of numbers and
# returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumulative_sum(input_value):
    '''this function addes a value then adds with the previous value to get its
    next value'''
    cumulative_list = []
    '''i create a for loop to enumerate through the input values'''
    for index, value in enumerate(input_value):
        '''the first value cannot be added since there is no previous value, 
        so if index is 0 just store the first value into our new list'''
        if index == 0:
            cumulative_list.append(value)
        else:
            '''now we want to add the next value with the previous value.  Not
            to get confused, we are taking value from our loop and adding it
            to our new list cumulative_list's previous value'''
            cumulative_list.append(int(value) + int(cumulative_list[index-1]))
    return cumulative_list
       
print(cumulative_sum([1,2,3,3,3,3,3]))

# Additional Exercise

# Once you've completed the above exercises, follow the directions
# from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# Bonus

# Create a function named twelveto24. It should accept a string in the format
# 10:45am or 4:30pm and return a string that is the representation of the time
# in a 24-hour format.

def twelveto24(input_value):
    time = ""
    am_pm = ""
    '''using a for loop to ignore the numbers and give us only the none digit
    values.  We should be left with only am or pm.  I created a am_pm variable
    that we will store this information too'''
    for value in input_value:
        if value not in "0123456789:":
            am_pm += value
    '''now our for loop is taking in only our digits for the time'''
    for value in input_value:
            if value in "0123456789":
                time +=value
    '''if "am", the math is different than pm so we had to split it up'''
    if am_pm == 'am':
        time_value = int(time)
        '''if the time is 1200 than military time is 00 so we had to subtract
        here'''
        if time_value in range(1200, 1260):
            time_value = time_value - 1200
            '''a lil string manipulation to add some leading zeros an the
            word hours'''
            if len(str(time_value)) == 2:
                return "00" + str(time_value) + " hours"
            elif len(str(time_value)) == 1:
                return "000" + str(time_value) + " hours"
            '''if its not 12 the its no problem, just return the time with a leading 0'''
        
        else:
            if(len(time) == 3):
                return "0"+time + " hours"
            else:
                return time + " hours"
        '''if pm, no special cases in pm, just add 1200 to time and we are good'''
    elif am_pm == "pm":
        time_value = int(time)
        time_value = time_value + 1200
        return str(time_value) + " hours"


print(f"12:01am {twelveto24('12:01am')}")
print(f"12:35am {twelveto24('12:35am')}")
print(f"11:10am {twelveto24('11:10am')}")
print(f"10:05am {twelveto24('10:05am')}")
print(f"9:01am  {twelveto24('9:01am')}")
print(f"09:59am {twelveto24('09:59am')}")
print(f"8:55am  {twelveto24('8:55am')}")
print(f"08:13am {twelveto24('08:13am')}")
print(f"07:22am {twelveto24('07:22am')}")
print(f"7:15am  {twelveto24('7:15am')}")
print(f"06:45am {twelveto24('06:45am')}")
print(f"6:30am  {twelveto24('6:30am')}")
print(f"12:59am {twelveto24('12:59am')}\n")

print(f"1:01pm  {twelveto24('1:01pm')}")
print(f"10:35pm {twelveto24('10:35pm')}")
print(f"12:10pm {twelveto24('12:10pm')}")
print(f"10:05am {twelveto24('10:05pm')}")
print(f"9:01pm  {twelveto24('9:01pm')}")
print(f"09:59pm {twelveto24('09:59pm')}")
print(f"8:55pm  {twelveto24('8:55pm')}")
print(f"08:13pm {twelveto24('08:13pm')}")
print(f"07:22pm {twelveto24('07:22pm')}")
print(f"7:15pm  {twelveto24('7:15pm')}")
print(f"06:45pm {twelveto24('06:45pm')}")
print(f"6:30pm  {twelveto24('6:30pm')}")
print(f"12:59pm {twelveto24('12:59pm')}\n")




#Bonus write a function that does the opposite.

def twentyfour_to_12(input_value):
    '''this function is going from military time to normal time'''
    time_value = int(input_value)
    am_pm = ""
    time = ""
    
    if time_value <1200:
        am_pm = 'am'
    else:
        am_pm = 'pm'
        
    '''after i set the time and am_pm variable above, i used ranges to
    calculate whether i had to add or subtract 1200.  some extra ranges were
    seperated to make the string look good by adding leading zeros'''
    if time_value < 100:
        time_value += 1200
        time = str(time_value)
        '''notice i am using slice'''
        return time[0:2] + ":" + time[2:4] + am_pm
    elif time_value < 1000:
        time = str(time_value)
        return time[0:1] + ":" + time[1:3] + am_pm
    elif time_value < 1260:
        time = str(time_value)
        return time[0:2] + ":" + time[2:4] + am_pm
    elif time_value < 2100:
        time_value -= 1200
        time = "0"+ str(time_value)
        return time[0:2] + ":" + time[2:4] + am_pm
    elif time_value < 2500:
        time_value -= 1200
        time = str(time_value)
        return time[0:2] + ":" + time[2:4] + am_pm

print(f"1730  {twentyfour_to_12('1730')}")
print(f"1530  {twentyfour_to_12('1530')}")
print(f"2430  {twentyfour_to_12('2430')}")
print(f"0001 {twentyfour_to_12('0001')}")
print(f"1201 {twentyfour_to_12('1201')}")
print(f"1235 {twentyfour_to_12('1235')}")
print(f"1110 {twentyfour_to_12('1110')}")
print(f"1005 {twentyfour_to_12('1005')}")
print(f"901  {twentyfour_to_12('901')}")
print(f"0959 {twentyfour_to_12('0959')}")
print(f"855  {twentyfour_to_12('855')}")
print(f"0813 {twentyfour_to_12('0813')}")
print(f"0722 {twentyfour_to_12('0722')}")
print(f"715  {twentyfour_to_12('715')}")
print(f"0645 {twentyfour_to_12('0645')}")
print(f"630  {twentyfour_to_12('630')}")
print(f"1259 {twentyfour_to_12('1259')}\n")

print(f"101  {twentyfour_to_12('101')}")
print(f"1035 {twentyfour_to_12('1035')}")
print(f"1210 {twentyfour_to_12('1210')}")
print(f"1005 {twentyfour_to_12('1005')}")
print(f"901  {twentyfour_to_12('901')}")
print(f"0959 {twentyfour_to_12('0959')}")
print(f"855  {twentyfour_to_12('855')}")
print(f"0813 {twentyfour_to_12('0813')}")
print(f"0722 {twentyfour_to_12('0722')}")
print(f"715  {twentyfour_to_12('715')}")
print(f"0645 {twentyfour_to_12('0645')}")
print(f"630  {twentyfour_to_12('630')}")
print(f"1259 {twentyfour_to_12('1259')}\n")

# Create a function named col_index. It should accept a spreadsheet column
# name, and return the index number of the column.

def col_index(input_value):
    '''I created a dictionary called mydict, with keys as A-Z, and values of 
    1-26 respectively'''
    
    mydict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
        }
    answer = 0
    '''created a loop where the index represents how many times we cycled
    through a-z, which is 26 char, so adding that to the current letters
    value'''
    for index, value in enumerate(input_value):
        answer = (26 * index) + mydict[value]
    return answer

print(col_index("A"))
print(col_index("B"))
print(col_index("C"))
print(col_index("AA"))
print(col_index("AAAA"))


