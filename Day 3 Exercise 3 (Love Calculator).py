# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Name1_In_Lowercase = name1.lower()

Name2_In_Lowercase = name2.lower()

Occurence_of_TRUE = ( (Name1_In_Lowercase.count("t") + Name2_In_Lowercase.count("t")) + (Name1_In_Lowercase.count("r") + Name2_In_Lowercase.count("r")) + (Name1_In_Lowercase.count("u") + Name2_In_Lowercase.count("u")) + (Name1_In_Lowercase.count("e") + Name2_In_Lowercase.count("e")) )

Occurence_of_LOVE = ( (Name1_In_Lowercase.count("l") + Name2_In_Lowercase.count("l")) + (Name1_In_Lowercase.count("o") + Name2_In_Lowercase.count("o")) + (Name1_In_Lowercase.count("v") + Name2_In_Lowercase.count("v")) + (Name1_In_Lowercase.count("e") + Name2_In_Lowercase.count("e")) )

LOVE_SCORE = ( str (Occurence_of_TRUE) + str (Occurence_of_LOVE) )

INT_OF_LOVE_SCORE = int(LOVE_SCORE)

if INT_OF_LOVE_SCORE < 10 or INT_OF_LOVE_SCORE > 90:
    print (f"Your score is {INT_OF_LOVE_SCORE}, you go together like coke and mentos.")

elif INT_OF_LOVE_SCORE > 40 and INT_OF_LOVE_SCORE < 50:
    print (f"Your score is {INT_OF_LOVE_SCORE}, you are alright together.")

else:
    print (f"Your score is {INT_OF_LOVE_SCORE}.")