print("Welcome to Hogwarts.")
print("Your mission is to find save Dumbledore.")

choice1 = input("You enter Hogwarts and decide whether to rest in the dining room on the right or the two rooms on the left. Which way do you turn? Right or left?\n").lower()
if choice1 == "left":
    choice2 = input("Great, you meet Ron, who helps you.You can't find your wand to save Dumbledore. What are you gonna do? Borrow a wand from Ron - write R, or send Hedwig to get a new one - write N.\n").lower()
    if choice2 == "n":
        choice3 = input("Great, Hedvika is reliable and you've got your wand and can continue your rescue.You found Dumbledore locked in the chamber. What are you going to do? Call for help unlock it.\n").lower()
        if choice3 == "unlock":
            print("Great, you saved Dumbledore.")
        else: 
            print("Ron's wand never worked, unfortunately it froze you and you didn't save Dumbledore. Game over")
    else: 
        print("Ron's wand never worked, unfortunately it froze you and you didn't save Dumbledore. Game over")
else: 
    print("The Brain Chamber is taking you to jail. You didn't save Dumbledore. Game over")