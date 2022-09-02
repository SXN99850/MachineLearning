# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
import math

# Take user input of weights in lbs
Number_of_students = int(input("Enter No.of students: "))
print("Enter", Number_of_students, "students weights")
weights_in_lbs = []
for i in range(0, Number_of_students):
    weight = int(input())
    weights_in_lbs.append(weight)

print(Number_of_students)
print("weights in lbs", weights_in_lbs)

# converting lbs to kilograms
weights_in_kgs = []
for i in range(0, Number_of_students):
    #use math.floor to round down a number to a nearest integer
    weights_in_kgs.append(math.floor((weights_in_lbs[i] / 2.2046) * 100) / 100)
print("Weights in kilograms", weights_in_kgs)
