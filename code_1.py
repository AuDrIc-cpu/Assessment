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
input("What is your name? ") 

#To make sure that they put a number on the camp age 
while camp_age == "" or camp_age.isdigit() == False :
  camp_age = input("What is your age? ")
  if camp_age == "" or camp_age.isdigit() == False: print("you need to enter your age.")

#no more question if you dont reach the eligibility 
while int(camp_age) > age_min and int(camp_age) < age_max : 
if age >= camp_leader_age :
  print("You are also eligible to be a camp leader!")
if age < age_min :
    int(input("What number camp do you want to go to? "))
    input(f"What meal do you want?: standard, vegan or veganvegan ")
    input(f"Do you need shuttle bus? extra cost is $80 ")
elif  Shuttle != "yes": 
  print("alright") 
  print("Alright so you picked number {num[1]} which is {activities[1]} and is {difficulty[1]}, your total is {cost[1]} ")
    

