#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = int(input("What was the total bill? RM "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = total * tip_as_percent
total_bill = total + total_tip_amount
bill_per_person = total_bill / people

#Round function does not provide the correct decimal spaces
#final_amount = round(bill_per_person, 2)
#Needed to use this line to provide the correct decimal spaces
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay RM {final_amount}")