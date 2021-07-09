# You have rented some movies for your kids: The little mermaid (for 3 days),
# Brother Bear (for 5 days, they love it), and Hercules (1 day,
# you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?

def cost_calculator(number_of_days):
    return (number_of_days * 3)

print("A 9 day rental would cost " + str(cost_calculator(9)) + " dollars.\n")

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
    print('\nis class full? Enter y/n only\n')
    class_full = input()
    if(class_full == 'N' or class_full=='n'):
        print('\nDoes the class schedule does not conflict with her current schedule? Enter y/n only\n')
        conflict = input()
        if(conflict == 'N' or conflict=='n'):
            print("\nStudent can be enrolled\n")
        elif(conflict =='Y' or conflict=='y'):
            print("\nStudent cannot be enrolled due to conflicting schedule\n")
        else:
            print(chr(27) + "[2J")
            print("\nPlease make a valid selection.\n")
            student_enrollment()
    elif(class_full == 'Y' or class_full=='y'):
        print("\nStudent cannot be enroleld due to class being full\n")
    else:
        print(chr(27) + "[2J")
        print("\nPlease make a valid selection.\n")
        student_enrollment()

student_enrollment()