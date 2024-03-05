# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
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

print("Enter the option : rock, paper, scissors")
ans=input().lower()

if ans=="rock":
    print("You chose")
    print(rock)
    res="rock"
elif ans == "paper":
    print("You chose")
    print(paper)
    res="paper"
elif ans == "scissors":
    print("You chose")
    print(scissors)
    res="scissors"
else:
    print("You chose a wrong option, Restart the game")
    exit()


gen=random.randint(0,2)
print("Computer chose")
if gen==0:
    print(rock)
    out="rock"
elif gen==1:
    print(paper)
    out="paper"
else:
    print(scissors)
    out="scissors"

if res=="rock" and out=="scissors":
    print("You win")
elif res=="scissors" and out=="paper":
    print("You win")
elif res=="paper" and out=="rock":
    print("You win")
elif res=="rock" and out=="rock":
    print("It's a draw")
elif res=="paper" and out=="paper":
    print("It's a draw")
elif res=="scissors" and out=="scissors":
    print("It's a draw")
else:
    print("You lose")
