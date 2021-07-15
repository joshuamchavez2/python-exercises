import function_master, itertools, json
from function_master import calculate_tip

# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
#print(function_master.is_vowel("a"))

# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip
# function directly. Call this function with values you choose and print the result.
#calculate_tip(15, 100)

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
#print(len(list(itertools.combinations("ABC123", 2))))
#print(list(itertools.combinations("ABC123", 2)))

# How many different combinations are there of 2 letters from "abcd"?
#print(len(list(itertools.combinations("ABC", 2))))
#print(list(itertools.combinations("ABC", 2)))

# How many different permutations are there of 2 letters from "abcd"?
#print(len(list(itertools.permutations("ABCD", 2))))
#print(list(itertools.permutations("ABCD", 2)))

# [
#     {
#       "_id": "54e23c3e46ab53a440b580e8",
#       "index": 0,
#       "guid": "9962b468-ef3e-4993-b677-617469bc3008",
#       "isActive": false,
#       "balance": "$2,097.02",
#       "picture": "http://placehold.it/32x32",
#       "age": 39,
#       "eyeColor": "blue",
#       "name": "Hebert Estes",
#       "gender": "male",
#       "company": "ANDRYX",
#       "email": "hebertestes@andryx.com",
#       "phone": "+1 (866) 456-2268",
#       "address": "121 Emmons Avenue, Klondike, Kentucky, 5975",
#       "about": "Sit cillum deserunt irure laboris tempor fugiat laboris. Amet commodo amet est incididunt. Dolore qui fugiat cillum pariatur dolore excepteur elit ipsum.\r\n",
#       "registered": "2014-11-10T01:44:03 +06:00",
#       "latitude": -80.157843,
#       "longitude": 161.93016,
#       "tags": [
#         "sit",
#         "occaecat",
#         "non",
#         "ea",
#         "sit",
#         "laboris",
#         "exercitation"
#       ],
#       "friends": [
#         {
#           "id": 0,
#           "name": "Tanisha Leonard"
#         },
#         {
#           "id": 1,
#           "name": "Dennis Wilson"
#         },
#         {
#           "id": 2,
#           "name": "Lupe Howe"
#         }
#       ],
#       "greeting": "Hello, Hebert Estes! You have 4 unread messages.",
#       "favoriteFruit": "strawberry"
#     }
profiles = json.load(open('profiles.json'))

#total numbers of users
def total_number_of_users():
    return len(profiles)

#print(total_number_of_users())

# Number of active users
def isActive(isacitive=True):
    count = 0
    for profile in profiles:
        if  profile["isActive"]==isacitive:
            count +=1
    return count

#print(isActive(True))

# Number of inactive users
#print(isActive(False))

# Grand total of balances for all users
def total_of_balances():
    total_balance=0.00
    balance = 0.00
    for profile in profiles:
        balance = remove_chars_from_currency(profile["balance"])
        balance = convert_to_float(balance)
        total_balance +=balance
    return total_balance

def convert_to_float(input_value):
    return float(input_value)

def remove_chars_from_currency(input_value):
    currency = ""
    for value in input_value:
        if value not in "$,":
            currency +=value
    return currency


#print(total_of_balances())

# Average balance per user
def avg_balance():
    return total_of_balances()/total_number_of_users()

# print(avg_balance())

# User with the lowest balance

def find_min_balance():
    return min(profiles, key=lambda x: x["balance"])["balance"]

#print(find_min_balance())

# User with the highest balance
def find_max_balance():
    return max(profiles, key=lambda x: x["balance"])["balance"]
#print(find_max_balance())


# Most common favorite fruit
def most_common_fruit():
    fruits=[]
    for profile in profiles:
        fruits.append(profile["favoriteFruit"])
    return max(fruits, key=fruits.count)

#print(most_common_fruit())
# Least most common favorite fruit
def least_common_fruit():
    fruits=[]
    for profile in profiles:
        fruits.append(profile["favoriteFruit"])
    return min(fruits, key=fruits.count)

#print(least_common_fruit())

# Total number of unread messages for all users

def strip_string_for_number(input_value):
    number = ''
    for value in input_value:
        if value in "0123456789":
            number += value
    return int(number)


def total_unread_messages():
    total = 0
    for profile in profiles:
        total += strip_string_for_number(profile["greeting"])
    return total

print(total_unread_messages())