import function_master, itertools, json
from function_master import calculate_tip

# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
print(function_master.is_vowel("a"))

# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip
# function directly. Call this function with values you choose and print the result.
calculate_tip(15, 100)

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
print(len(list(itertools.combinations("ABC123", 2))))
print(list(itertools.combinations("ABC123", 2)))

# How many different combinations are there of 2 letters from "abcd"?
print(len(list(itertools.combinations("ABC", 2))))
print(list(itertools.combinations("ABC", 2)))


# How many different permutations are there of 2 letters from "abcd"?
print(len(list(itertools.permutations("ABCD", 2))))
print(list(itertools.permutations("ABCD", 2)))



profiles = json.load(open('profiles.json'))

