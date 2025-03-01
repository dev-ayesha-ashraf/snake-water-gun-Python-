import random
computerChoice = ["snake" , "water" , "gun"]
randomGenerate = random.choice(computerChoice)
computer = randomGenerate
you = input("Enter Your Choice: ")
print(f"computer chose {computer} and you chose {you}")
if(computer == you):
    print("It's a Draw")
else:
    if(computer == "snake" and you == "water"):
        print("you Lose")
    elif(computer == "water" and you == "snake"):
        print("You won")
    elif(computer == "water" and you == "gun"):
        print("You Lose")
    elif(computer == "gun" and you == "water"):
        print("You Won")
    elif(computer == "gun" and you == "snake"):
        print("You Lose")
    elif(computer == "snake" and you == "gun"):
        print("You won")
    else:
        print("something went wrong")