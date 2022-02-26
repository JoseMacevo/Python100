#  Don't change the code below 👇🚨

student_scores = input("Insert a list of student_scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# 🚨 Don't change the code above 👆

reference = 0
new_list = []
for score in student_scores:
    if score >= reference:
        reference = score
        new_list.clear()
        new_list.append(reference)
print(f"The highest score in the class is: {new_list[0]}")

