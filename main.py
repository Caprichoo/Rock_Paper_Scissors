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
print("Welcome to Rock Paper Scissors")
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
else:
    print(scissors)
print(f'Your input is {user_input}')
#random.randint[]

