from random import randint
print("Welcome to Python Casino!")
Player = int(input("Choose number\n"))

Banker = randint(1,10)
playing = True
    
while playing:
    if Player == Banker:
        print("Banker is", Banker, "!")
        print("Tie!")
        playing = False
    elif Player > Banker:
        print("Banker is", Banker, "!")
        print("You won!")
        playing = False
    
    elif Player < Banker:
        print("Banker is", Banker, "!")
        print("You lose!")
        playing = False