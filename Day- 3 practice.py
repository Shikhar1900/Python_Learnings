Height = int (input ( "Please enter your height (in cm) : ") )

if Height >= 120:
    print ("You can ride the rollercoaster")
    Age = int ( input ("Please enter your age: "))
    bill = 0
    if Age < 12:
        bill += 5
    elif Age <= 18:
        bill += 7
    elif Age >= 45 and Age <= 55:
        bill += 0
        print ("Your ride is on us")
    else:
        bill += 12

    Photos = input ("Do you want photos Y or N: ")
    if Photos == "Y":
      bill += 3
      print (f"Your total bill is {bill}")

    else:
        print (f"Your total bill is {bill}")

 

else:
    print ("You cannot ride the rollercoaster")