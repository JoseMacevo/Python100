#  Don't change the code below 👇🚨

student_heights = input("Insert a list of student_heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#  🚨 Don't change the code above 👆
'''
Whithout using neither len() nor sum() functions, the only way to realice 
this exercise is creating two variables
sum_elem and a counter.
'''
sum_elem = 0
counter = 0
for i in student_heights:
    sum_elem = sum_elem + i  # Sum of elements.
    counter += 1  # Number of turns giver by the loop

final_average = round(sum_elem / counter)
print(final_average)



