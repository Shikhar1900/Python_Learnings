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

# Write your code below this line 👇



Your_Response = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors"))

import random

Computer_Chose = random.randint(0,2)

# if Computer_Chose == 0:
# A = rock

# # elif Computer_Chose == 1:
# B = paper

# # elif Computer_Chose == 2:
# C = scissors 

# print (C)

Game_Images = [rock, paper, scissors]

print (Game_Images[Your_Response])

# print (Computer_Chose)
if Your_Response == Computer_Chose:
    print ("Computer Chose:")
    print (Game_Images[Computer_Chose])
    print ("Game Tied")

# Rock wins against scissors:

elif Your_Response == 0 and Computer_Chose == 2:
    # E = (rock + \n + "Computer_Chose")
    print ("Computer Chose:")
    print (Game_Images[Computer_Chose])
    print ("You Win")



# Scissors win against paper:

elif Your_Response == 2 and Computer_Chose == 1:
    print ("Computer Chose:")
    print (Game_Images[Computer_Chose])
    print ("You Win")


# Paper wins against rock:

elif Your_Response == 1 and Computer_Chose == 0:
    print ("Computer Chose:")
    print (Game_Images[Computer_Chose])
    print ("You Win")

else:
    print ("Computer Chose:")
    print (Game_Images[Computer_Chose])
    print ("You lose")


