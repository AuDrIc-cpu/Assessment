#list
num = ["0","1","2"]
food = ["standard","vegan","veganvegan"]
activities = ["Cultural immersion","Kayaking & pancakes","Mountain bike"]
difficulty = ["easy","moderate","hard"]
cost = ["800","400","900"]
age_min = 5
age_max = 17
age = 0
camp_leader_age = 15
Shuttle = ""
camp_age = ""
 
#print
print("num    activities              difficulty             cost")    
print("0    Cultural immersion          easy                  800")
print("1     Kayaking & pancakes       moderate               400")
print("2       Mountain bike           hard                   900")
 
#questions for the person who is taking the order thingy  
name = input("What is your name? ")  
 
#To make sure that they put a number on the camp age
while camp_age == "" or camp_age.isdigit() == False:
    camp_age = input("What is your age? ")
    if camp_age == "" or camp_age.isdigit() == False:
        print("You need to enter your age.")


#eligibility for camp leader age 
if (camp_age) > camp_leader_age and int(camp_age) < age_max print(f"{camp_age} You are qualified to get camp leader!")
 
camp_number = input("Enter camp number (0, 1, or 2): ")  
 
Shuttle = input("Do you need a shuttle bus? Extra cost is $80: ")
 
if Shuttle == "yes":
    print("Shuttle booked.")
elif Shuttle != "yes":  
    print(f"Alright {name}, you picked camp {num[int(camp_number)]} which is {activities[int(camp_number)]}, difficulty {difficulty[int(camp_number)]}.") # FIX 5: removed extra )"