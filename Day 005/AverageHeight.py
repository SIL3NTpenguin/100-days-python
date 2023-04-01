# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sumHeight = 0
countStudent = len(student_heights)
for height in student_heights:
    sumHeight += height

print(round(sumHeight/countStudent))
