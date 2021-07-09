# You have rented some movies for your kids: The little mermaid (for 3 days),
# Brother Bear (for 5 days, they love it), and Hercules (1 day,
# you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?

def cost_calculator(number_of_days):
    print(chr(27) + "[2J")
    return (number_of_days * 3)

print("A 9 day rental would cost " + str(cost_calculator(9)) + " dollars.\n\n")

# Suppose you're working as a contractor for 3 companies: Google,
# Amazon and Facebook, they pay you a different rate per hour.
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
# How much will you receive in payment for this week?
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.


def payment_calculator(facebook_hours, google_hours, amazon_hours):
    total = (facebook_hours*350) + (google_hours*400) + (amazon_hours*380)
    return total
print("10 hours at Facebook, 6 hours at Google, and 4 hours at Amazon would pay " + str(payment_calculator(10, 6, 4)) + " dollars.\n")

# A student can be enrolled to a class only if the class is
# not full and the class schedule does not conflict with her current schedule.

def student_enrollment():
    print('\nIs class full? Enter y/n only\n')
    two_items = input()
    if(two_items == 'N' or two_items=='n'):
        print('\nDoes the class schedule does not conflict with her current schedule? Enter y/n only\n')
        conflict = input()
        if(conflict == 'N' or conflict=='n'):
            print("\nStudent can be enrolled\n")
        elif(conflict =='Y' or conflict=='y'):
            print("\nStudent cannot be enrolled due to conflicting schedule\n")
        else:
            
            print("\nPlease make a valid selection.\n")
            student_enrollment()
    elif(two_items == 'Y' or two_items=='y'):
        print("\nStudent cannot be enroleld due to class being full\n")
    else:
        
        print("\nPlease make a valid selection.\n")
        student_enrollment()

student_enrollment()

# A product offer can be applied only if people buys more than 2 items,
# and the offer has not expired.
# Premium members do not need to buy a specific amount of products.

def two_item_check():

    print('\nDid you buy more than two items? Enter y/n only.\n')
    two_items = input()
    if(two_items == 'N' or two_items=='n'):
        print('\nYou cannot recieve the product offer because you need to buy 2 or more items for the product offer.\n')
        return False
    elif(two_items == 'Y' or two_items=='y'):
        return True
    else:
        print(chr(27) + "[2J")
        print('\nPlease enter a valid selection.\n')
        return two_item_check()
        

def offer_expired_check():
    
    print('\nIs your offer expired? Enter y/n only.\n')
    offer_expired = input()
    if(offer_expired == 'N' or offer_expired=='n'):
        return True
    elif(offer_expired == 'Y' or offer_expired=='y'):
        print('\nYou cannot recieve the product offer because your offer is expired.\n')
        return False
    else:
        
        print('\nPlease enter a valid selection.\n')
        return offer_expired_check()

def premium_members_check():
   
    print('\nAre you a premium member? Enter y/n only.\n')
    premium_member = input()
    if(premium_member=='Y' or premium_member=='y'):
        return True
    elif(premium_member=='N' or premium_member=='n'):
        return False
    else:
        
        print('\nPlease enter a valid selection.\n')
        return premium_members_check()

def product_offer():
    if(premium_members_check()==True):
        
        print('\nYou are eligible for the product offer.\n')
    elif(offer_expired_check() == True and two_item_check() == True):
        
        print('\nYou are eligible for the product offer.\n')

   

product_offer()