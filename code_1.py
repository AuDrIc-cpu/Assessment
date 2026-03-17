#list 
num = ["0","1","2"]
food = ["standard","vegan","veganvegan"]
activities = ["Cultural immersion","Kayaking & pancakes","Mountain bike"]
difficulty = ["easy","moderate","hard"]
cost = ["800","400","900"]

#print 
print("num    activities              difficulty             cost")    
print("0    Cultural immersion          easy                  800")
print("1     Kayaking & pancakes       moderate               400")
print("2       Mountain bike           hard                   900")
 
#questions for the person who is taking the order thingy  
input("What is your name? ") 
int(input(f"What is your age? "))
age = 0
if age<13 :
    int(input("What number camp do you want to go to? "))
    input(f"What meal do you want?: standard, vegan or veganvegan ")
    input(f"Do you need shuttle bus? extra cost is $80 ")
if  Shuttle != yes: 
  print("alright") 
  print("Alright so you picked number {num[1]} which is {activities[1]} and is {difficulty[1]}, your total is {cost[1]} ")
elif age > 12 : 
  print("sorry you are not eligible to come.")    