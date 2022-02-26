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

possible_choices = [rock, paper, scissors]
choose = len(possible_choices)
user_choice = int(input("What do you choose?, type 0 for Rock, 1 for Paper and 2 for scissors: "))
computer_choice = random.randint(0, choose - 1)

if user_choice != computer_choice:
    if user_choice == 0 and computer_choice == 1:
        print(f"Your choice was: {possible_choices[0]}\nComputer selection is: {possible_choices[1]}\n"
              f"YOU LOOSE")
    elif user_choice == 0 and computer_choice == 2:
        print(f"Your choice was: {possible_choices[0]}\nComputer selection is: {possible_choices[2]}\n"
              f"YOU WIN")
    elif user_choice == 1 and computer_choice == 0:
        print(f"Your choice was: {possible_choices[1]}\nComputer selection is: {possible_choices[0]}\n"
              f"YOU WIN")
    elif user_choice == 1 and computer_choice == 2:
        print(f"Your choice was: {possible_choices[1]}\nComputer selection is: {possible_choices[2]}\n"
              f"YOU LOOSE")
    elif user_choice == 2 and computer_choice == 0:
        print(f"Your chice was: {possible_choices[2]}\nComputer selection is: {possible_choices[0]}\n"
              f"YOU LOOSE")
    elif user_choice == 2 and computer_choice == 1:
        print(f"Your chice was: {possible_choices[2]}\nComputer selection is: {possible_choices[1]}\n"
              f"YOU WIN")
    else:
        print("INVALID SELECTION GAME OVER")
else:
    if user_choice == 0 and computer_choice == 0:
        print(f"Your choice was: {possible_choices[0]}\nComputer selection is: {possible_choices[0]}\n"
              f"DRAW")
    elif user_choice == 1 and computer_choice == 1 :
        print(f"Your chice was: {possible_choices[1]}\nComputer selection is: {possible_choices[1]}\n"
              f"DRAW")
    elif user_choice == 2 and computer_choice == 2:
        print(f"Your choice was: {possible_choices[2]}\nComputer selection is: {possible_choices[2]}\n"
              f"DRAW")



