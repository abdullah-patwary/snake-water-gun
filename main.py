import random

def decision(computer, myTurn):
    if computer == myTurn:
        return None
    elif computer == 1:
        if myTurn == 2:
            return False
        elif myTurn == 3:
            return True
    elif computer == 2:
        if myTurn == 1:
            return True
        elif myTurn == 3:
            return False
    elif computer == 3:
        if myTurn == 1:
            return False
        elif myTurn == 2:
            return True

print("Do you want to know about myself?")
start = int(input("Press 1 for Yes and Press 2 for NO: "))
if start == 1:
    with open("Read.txt", "rt") as file:
        f = file.read()
        print(f)
    game = input("Press y to continue and n for exit: ")
    if game == "y":
        print("Computer's Turn: ****")
        computer = random.randint(1, 3)
        myTurn = int(input("Enter 1 for (Snake),  2 for (Water), 3 for (Gun)\n--> "))
        ######
        result = decision(computer, myTurn)
        if computer == 1:
            computer = "Snake"
        elif computer == 2:
            computer = "Water"
        else:
            computer = "Gun"
            ######
        if myTurn == 1:
            myTurn = "Snake"
        elif myTurn == 2:
            myTurn = "Water"
        else:
            myTurn = "Gun"
            ######
        print(f"Computer select: {computer}")
        print(f"You select: {myTurn}")
        if result == None:
            print("Match is draw")
        elif result == True:
            print("You Win the Game!")
        else:
            print("You Lose the Game!")

    else:
        print("Thank you")
else:
    print("Thank you")
    exit()