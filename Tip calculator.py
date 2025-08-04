print("_"*50)
print("welcome to tip calculator!")
print("-"*50)
bill=float(input("enter total amount:"))
tip=int(input("enter the tip percentage would you give:"))
people=int(input("enter how many numbers you want to split bill:"))
tip_percentage=tip/100
total_tip_amount=bill*tip_percentage
total_bill=bill+total_tip_amount
each_person=total_bill/people
print("each person should pay:",each_person)
