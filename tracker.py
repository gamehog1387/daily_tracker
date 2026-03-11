import json

def save_data(all_habits):
    with open("habits.json", "w") as f:
        json.dump(all_habits, f, indent=4)
    print("---DATA SAVED TO DISK----")


def load_data():
    filename = "habits.json"
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def ADD_hours_studying():
    while True:
        try:
            hours = input("Enter Hours studied ")
            struggle = input("What are you struggling with? ")
        except ValueError:
            print("Invalid input")
        data = {
            "hours": hours,
            "struggle": struggle,
        }
        break
    return data

def add_time_gym():
    while True:
        try:
            time_spent = input("Time spent at gym? hours/minutes example:2:44 ")
            was_it_waste = input("Did you waste your time? ")
            plan_tommorow = input("Whats plan for tmr? Are you going again or resting? ")
        except ValueError:
            return "Incorrect input"
        data = {
            "time_spent": time_spent,
            "was_it_waste": was_it_waste,
            "plan_tommorow": plan_tommorow,

        }
        break
    return data

        
data = load_data()
studying = data.get('studying', {})
gymtime = data.get('gymtime', {})
save_data
while True:

    print("\nMy Daily habits")
    print("1. ADD - How many hours did you study?")
    print("2. View hours studied")
    print("3. ADD - Time spent at gym?")
    print("4. View time spent at the gym")
    choice = input("What would you like to ADD? ")
    if choice == '1.' or choice == '1':
        save_data({"studying": studying, "gymtime": gymtime})
        studying = ADD_hours_studying()
        print("Progress saved")
        
    elif choice == '2' or choice == '2.':
        print(f"Good work so far! {studying['hours']} Hours have been spent studying.\nYou are currently struggling with {studying['struggle']}. ")

    elif choice == '3' or choice == '3.':
        save_data({"studying": studying, "gymtime": gymtime})
        gymtime = add_time_gym()
        print("Gym time has been saved.")
    elif choice == '4' or choice == '4.':\
        print(f"You spent {gymtime['time_spent']} time at the gym, you wasted {gymtime['was_it_waste']} hours:minutes at the gym/nYour plan tommorow is {gymtime['plan_tommorow']}, good luck!")
       
       
        
