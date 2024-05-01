import random

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

#Write your code below this line 👇
game_images = [rock, paper,scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_input >= 3 or player_input < 0:
    print("You typed an invalid number. You lose!")
else:
    print(game_images[player_input])

    computer_input = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_input])

    if player_input == 0 and computer_input == 2:
        print("You win!")
    elif computer_input == 0 and player_input == 2:
        print("You lose!")
    elif computer_input > player_input:
        print("You lose!")
    elif player_input > computer_input:
        print("You win!")
    elif computer_input == player_input:
        print("It's a draw!")
