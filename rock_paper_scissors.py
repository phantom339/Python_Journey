# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=int(input("What do you choose? Stone -0, Paper -1, scissors -2? "))
comp=random.randint(0,2)
if choice==0 and comp==0:
    print("Your choice.")
    print(rock)
    print("Computers choice.")
    print(rock)
    print("Draw")
elif choice==0 and comp==1:
    print("Your choice.")
    print(rock)
    print("Computers choice.")
    print(paper)
    print("You lose")
elif choice==0 and comp==2:
    print("Your choice.")
    print(rock)
    print("Computers choice.")
    print(scissors)
    print("You win") 
elif choice==1 and comp==0:
    print("Your choice.")
    print(paper)
    print("Computers choice.")
    print(rock)
    print("You win") 
elif choice==1 and comp==1:
    print("Your choice.")
    print(paper)
    print("Computers choice.")
    print(paper)
    print("Draw")
elif choice==1 and comp==2:
    print("Your choice.")
    print(paper)
    print("Computers choice.")
    print(scissors)
    print("You lose") 
elif choice==2 and comp==0:
    print("Your choice.")
    print(scissors)
    print("Computers choice.")
    print(rock)
    print("You lose") 
elif choice==2 and comp==1:
    print("Your choice.")
    print(scissors)
    print("Computers choice.")
    print(paper)
    print("You win")  
elif choice==2 and comp==2:
    print("Your choice.")
    print(scissors)
    print("Computers choice.")
    print(scissors)
    print("Draw") 
else:
    print("Your selection in invalid")                















