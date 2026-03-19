num = ["0","1","2"]
food = ["standard","vegan","veganvegan"]
activities = ["Cultural immersion","Kayaking & pancakes","Mountain bike"]
difficulty = ["easy","moderate","hard"]
cost = ["800","400","900"]
 
age_min = 5
age_max = 17
camp_leader_age = 15
 
print("num    activities              difficulty             cost")    
print("0    Cultural immersion          easy                  800")
print("1    Kayaking & pancakes         moderate              400")
print("2    Mountain bike               hard                  900")
 
name = input("What is your name? ")
 
# ask for age correctly
camp_age = ""
while camp_age == "" or camp_age.isdigit() == False:
    camp_age = input("What is your age? ")
    if camp_age == "" or camp_age.isdigit() == False:
        print("You need to enter your age.")
 
camp_age = int(camp_age)
 
# check eligibility
if camp_age < age_min or camp_age > age_max:
    print("Sorry, you are not eligible for the camp.")
else:
    if camp_age >= camp_leader_age:
        print("You are also eligible to be a camp leader!")
 
    camp_number = input("What number camp do you want to go to? (0, 1, 2) ")
    meal = input("What meal do you want? standard, vegan or veganvegan: ")
    shuttle = input("Do you need the shuttle bus? (extra $80) yes/no: ")
 
    total_cost = int(cost[int(camp_number)])
 
    if shuttle.lower() == "yes":
        total_cost += 80
 
    print(f"Alright {name}, you picked camp {num[int(camp_number)]} which is {activities[int(camp_number)]}, difficulty {difficulty[int(camp_number)]}.")
    print(f"Your total cost is ${total_cost}.")