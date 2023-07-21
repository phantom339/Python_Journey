# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=weight/(height**2) 
final=round(bmi)
if final < 18.5:
    print(f"Your BMI is {final}, you are underweight.")
elif final < 25:
    print(f"Your BMI is {final}, you have a normal weight.")
elif final <30 :
    print(f"Your BMI is {final}, you are slightly overweight.")  
elif final < 35:
    print(f"Your BMI is {final}, you are obese.")         
else:
    print(f"Your BMI is {final}, you are clinically obese.")     