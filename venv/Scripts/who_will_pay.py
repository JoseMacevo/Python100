import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

# Write your code below this line 👇
item_num = len(names)
random_choice = random.randint(0, item_num - 1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay}, is going to buy our meal today..!")

