# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
l=0
sum=0
for height in student_heights:
    l+=1
    sum+=height
avg=sum/l
print(round(avg))    

    



