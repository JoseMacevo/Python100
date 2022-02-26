#  Don't change the code below 👇🚨

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# 🚨 Don't change the code above 👆

new_list = list(position)
columns = int(new_list[1])
rows = int(new_list[0])
map [columns - 1][rows -1] = 'X' 

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

