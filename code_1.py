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
 
#questions
name = input("What is your name? ")
 
#To make sure that they put a number on the camp age
while camp_age == "" or camp_age.isdigit() == False:
    camp_age = input("What is your age? ")
    if camp_age == "" or camp_age.isdigit() == False:
        print("You have to be within the age group of 5-17")
 
#eligibility for camp leader age
if int(camp_age) > camp_leader_age and int(camp_age) < age_max:
    print(f"{camp_age} You are qualified to get camp leader!")
 
camp_number = input("Enter camp number (0, 1, or 2): ")
meal = input(f"What meal do you want?: standard, vegetarian, vegan ")
 
Shuttle = input("Do you need a shuttle bus? Extra cost is $80: ")
 
# cost calculate
camp_cost = int(cost[int(camp_number)])
total_without_shuttle = camp_cost
total_with_shuttle = camp_cost + shuttle_cost
 
if Shuttle == "yes":
    print("Shuttle booked.")
    print(f"Alright {name}, you picked camp {num[int(camp_number)]} which is {activities[int(camp_number)]}, difficulty {difficulty[int(camp_number)]}, your meal is {meal}.")
    input(f"Please confirm you want to go with the cost of {total_with_shuttle} ")
    print("Enjoy the camp.")
elif Shuttle != "yes":
    print(f"Alright {name}, you picked camp {num[int(camp_number)]} which is {activities[int(camp_number)]}, difficulty {difficulty[int(camp_number)]}, your meal is {meal}.")
    input(f"Please confirm you want to go with the cost of: {total_without_shuttle} ")
if confirmation == "yes":
    print(f"Enjoy the camp.")
elif confirmation != "yes"
  print(f"Have a good day.")