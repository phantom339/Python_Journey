# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower1=name1.lower()
lower2=name2.lower()
T=lower1.count("t") + lower2.count("t")
R=lower1.count("r") + lower2.count("r")
U=lower1.count("u") + lower2.count("u")
E=lower1.count("e") + lower2.count("e")
TRUE=T+R+U+E
L=lower1.count("l") + lower2.count("l")
O=lower1.count("o") + lower2.count("o")
V=lower1.count("v") + lower2.count("v")
E2=lower1.count("e") + lower2.count("e")
Love=L + O + V + E2
final= str(TRUE) + str(Love)
score=int(final)
if score < 10 or score > 90:
     print(f"Your score is {score}, you go together like coke and mentos. ")
elif score >= 40 or score <= 50 :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")         

