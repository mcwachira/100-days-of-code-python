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

values = [rock,paper,scissors]
human_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))


if(human_choice <0 or human_choice > 2):
    print("Invalid Value try Again")
else:
    computer_choice = random.randint(0, len(values) - 1)

    print('You Choose:')
    print(values[human_choice])

    print ('Computer Choose:')
    print(values[computer_choice])

    if(values[human_choice] == values[computer_choice]):
        print('tie -Play again')
    elif(human_choice == 0 and computer_choice == 2) or (human_choice == 1 and computer_choice == 0) or (human_choice == 2 and computer_choice == 1):
        print("You  win and Computer lose")
    else:
        print('Computer Wins')

