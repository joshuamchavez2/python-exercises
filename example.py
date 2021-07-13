number = input("what number would you like to go up too?>")
num = int(number)
index = 1
stop_condition = False
while (stop_condition == False):
    num = int(number)
    #print("number  | squared  | cubed")
    #print("------  | -------  | -----")
    print(f"{'number': <7}|{'squared': ^7}|{'cubed': >3}")
    print(f"{'-------': <7}|{'-------': ^7}|{'------': >3}")
    while index <= num:
    #print(f"{index}      | {index**2}      | {index**3}")  
        print(f"{index: <7}|{index**2: ^7}|{index**3: >3}")
        index +=1
    stop_loop = input("Enter quit to exit or yes to continue>")
    if stop_loop.lower() == 'quit':
        stop_condition = True
    elif stop_loop.lower() == 'yes':
        number = input("what number would you like to go up too?>")
        index = 1
    else: 
        stop_condition = True