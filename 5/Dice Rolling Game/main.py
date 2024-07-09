import random
def roll():
    return random.randint(1,6)+random.randint(1,6) 

player1 = input("Enter player 1's name: \n")
player2 = input("Enter player 2's name: \n")
roll1 = roll()
roll2 = roll()
print(player1," rolled ",roll1)
print(player2," rolled ",roll2)

if roll1 > roll2:
    print(player1," wins!")
elif roll1==roll2:
    print("TIE")
else:
    print(player2," wins!")