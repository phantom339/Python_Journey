#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator") 
bill = float(input("what is your final bill :"))
tip = int(input("What is the percentage of tip you would like to give ?10 , 12 or 15 ? "))
person= int(input("How many persons are spliting the bill ? "))
bill_tip= tip/100 * bill + bill
bill_p=round(bill_tip/person , 2)
print(f"the amount of bill each person has to give : ${bill_p}")

