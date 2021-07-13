


def leading_spaces(input_value):
    
    cleaned_string = ""

    for index, value in enumerate(input_value):
        if value != " ":
            for i in range(index, len(input_value)):
                cleaned_string += input_value[i]
            break
        
    return cleaned_string

def reversed_string(input_value):
    reversed_string = ""
    for value in reversed(input_value):
        reversed_string += value
    return reversed_string

def trailing_spaces(input_value):

    flipped_string = ""
    cleaned_string = ""
    
    flipped_string = reversed_string(input_value)
    flipped_string = leading_spaces(flipped_string)
    
    cleaned_string = reversed_string(flipped_string)
    return cleaned_string


def number_as_start(input_value):
    cleaned_string = ""

    for index, value in enumerate(input_value):
        if value not in "123456790":
            for i in range(index, len(input_value)):
                cleaned_string += input_value[i]
            break
                
        
    return cleaned_string

def replace_spaces_with_underscore(input_value):
    cleaned_string = ""
    for value in input_value:
        if value == " ":
            cleaned_string += "_"
        else:
            cleaned_string += value
            
    return cleaned_string

def special_symbos(input_value):
    cleaned_string = ""

    for value in input_value:
        if value not in "~!@#$%^&*()+=-,.<>/?\|~;:[]{}":
            cleaned_string += value
    return cleaned_string

def string_to_lower_case(input_value):
    return input_value.lower()

def normalize_name(input_value):

    while input_value[0] in "0123456789 " or input_value[len(input_value)-1] in "0123456789 ":
        input_value = leading_spaces(input_value)
        input_value = trailing_spaces(input_value)
        input_value = number_as_start(input_value)
        input_value = special_symbos(input_value) 
       
    input_value = replace_spaces_with_underscore(input_value)
    input_value = string_to_lower_case(input_value)
    return input_value

test_code = "1 2 3 $()&^$( T#%^H#%^i%^s%^ i%^&S %&(*(a v$%&AlI#%^d p#%^YTh#%^on id#%^%&en$%&TI#$^%%$&^*Fi@$%^*(er  #^#^#@"

print(normalize_name(test_code))






