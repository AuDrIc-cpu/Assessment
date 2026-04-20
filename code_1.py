#list
num = ["0","1","2"]
food = ["standard","vegetarian","vegan"]
activities = ["Cultural immersion","Kayaking & pancakes","Mountain bike"]
difficulty = ["easy","moderate","hard"]
cost = ["800","400","900"]
age_min = 5
age_max = 17
age = 0
camp_leader_age = 15
Shuttle = ""
camp_age = ""
shuttle_cost = 80
confirmation = ""


#print
print("num    activities              difficulty             cost")    
print("0    Cultural immersion          easy                  800")
print("1     Kayaking & pancakes       moderate               400")
print("2       Mountain bike           hard                   900")

while True:
    #questions
    name ="" 
    while name == "" or name.isalpha() == False:
        name = input("What is your name?")
        if name == "" or name.isalpha() == False:
            print("you need to enter your name without numbers and without symbols")

                
    #To make sure that they put a number on the camp age
    camp_age = ""
    while camp_age == "" or camp_age.isdigit() == False:
        camp_age = input("What is your age? ")
        if camp_age == "" or camp_age.isdigit() == False:
            print("Please enter a valid age (numbers only).")
        elif int(camp_age) < age_min or int(camp_age) > age_max:
            print(f"Sorry, you are not able to come to the camp. You must be between {age_min} and {age_max}.")
            

    #eligibility for camp leader age
    if int(camp_age) > camp_leader_age and int(camp_age) < age_max:
        print(f"{camp_age} You are qualified to get camp leader!")

    camp_number = ""
    while camp_number not in ["0", "1", "2"]:
        camp_number = input("Enter camp number (0, 1, or 2): ")
        if camp_number not in ["0", "1", "2"]:
            print("Please enter a valid camp number: 0, 1, or 2.")

    #shuttle check
    while Shuttle.lower() not in  ["yes","no"]:
         Shuttle = input("Do you want to use the shuttle bus for an extra cost of $80? (yes/no)")
         if Shuttle.lower() not in ["yes","no"]:
              print("please choose yes or no")
    

    #cost calculate
    camp_cost = int(cost[int(camp_number)])
    total_without_shuttle = camp_cost
    total_with_shuttle = camp_cost + shuttle_cost

    #confirmation
    if Shuttle == "yes":
        print("Shuttle booked.")
        print(f"Alright {name}, you picked camp {num[int(camp_number)]} which is {activities[int(camp_number)]}, difficulty {difficulty[int(camp_number)]}, your meal is {meal}.")
        confirmation = input(f"Please confirm you want to go with the cost of {total_with_shuttle}: ")
    elif Shuttle != "yes":
        print(f"Alright {name}, you picked camp {num[int(camp_number)]} which is {activities[int(camp_number)]}, difficulty {difficulty[int(camp_number)]}, your meal is {meal}.")
        confirmation = input(f"Please confirm you want to go with the cost of: {total_without_shuttle}: ")

    if confirmation == "yes":
        print("Enjoy the camp.")
    
    else:
        print("Have a good day.")