computer_choice = 'scissors'
user_choice = input("rock, paper or scissors?")
if computer_choice == user_choice:
    print("tie")
elif computer_choice =="rock" and user_choice =="paper":
    print("user wins!")
elif computer_choice =="paper" and user_choice == "scissors":
    print("user wins!")
elif computer_choice =="scissors" and user_choice == "rock":
    print("user wins!")
else:
    print("computer wins")