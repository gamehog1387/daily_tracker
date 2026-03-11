def ADD_hours_studying():
    while True:
        try:
            hours = int(input("Enter Hours studied "))
            struggle = input("What are you struggling with? ")
        except ValueError:
            print("Invalid input")
        data = {
            "hours": hours,
            "struggle": struggle,
        }
        break
    return data

def add_time_gaming():
    while True:
        try:
            time_spent = int(input("Time spent gaming?"))
            was_it_waste = input("Did you waste your time?")
            plan_tommorow = input("Whats plan for tmr? Are you gaming or nah?")
        except ValueError:
            return"Incorrect input"
        data = {
            "time_spent": time_spent,
            "was_it_waste": was_it_waste,
            "plan_tommorow": plan_tommorow,

        }
        break
    return data
        
studying = {}
gamingtime = {}
while True:

    print("\nMy Daily habits")
    print("1. ADD - How many hours did you study?")
    print("2. View hours studied")
    print("3. ADD - Time spent at gym?")
    
    choice = input("What would you like to ADD? ")
    if choice == '1.' or choice == '1':
        studying = ADD_hours_studying()
        print("Progress saved")
        
    elif choice == '2' or choice == '2.':
        print(f"Good work so far! {studying['hours']} Hours have been spent studying.\nYou are currently struggling with {studying['struggle']}. ")

    elif choice == '3' or choice == '3.':
        gamingtime = add_time_gaming()
        print("Gaming time has been saved.")
