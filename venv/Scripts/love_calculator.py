print("Welcome to the Love Calculator")
name_1 = input("What's your name?: ")
name_2 = input("What's his/her name?: ")
name_t = name_1.upper().count("T")
name_r = name_1.upper().count("R")
name_u = name_1.upper().count("U")
name_e = name_1.upper().count("E")
my_name = name_t + name_r + name_u + name_e

sec_name_t = name_2.upper().count("T")
sec_name_r = name_2.upper().count("R")
sec_name_u = name_2.upper().count("U")
sec_name_e = name_2.upper().count("E")
her_name = sec_name_t + sec_name_r + sec_name_u + sec_name_e

name_t = name_1.upper().count("L")
name_r = name_1.upper().count("O")
name_u = name_1.upper().count("V")
name_e = name_1.upper().count("E")
my_name_l = name_t + name_r + name_u +name_e

sec_name_t = name_2.upper().count("L")
sec_name_r = name_2.upper().count("O")
sec_name_u = name_2.upper().count("V")
sec_name_e = name_2.upper().count("E")
her_name_l = sec_name_t + sec_name_r + sec_name_u + sec_name_e

true = str(my_name + her_name)
love = str(my_name_l + her_name_l)

true_love = true + love

score = int(true_love)

if score < 10 or score > 90:
    print(f"Your score is: {score} , you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you're allright together.")
else:
    print(f"Your score is: {score}")




