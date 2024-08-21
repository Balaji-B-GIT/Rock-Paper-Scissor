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

import random
choice = int(input("1..rock\n2..paper\n3..scissors\n"))
ai = random.randint(1,3)


if choice == 1:
  print(rock)
elif choice == 2:
  print(paper)
elif choice == 3:
  print(scissors)

if choice >3 or choice < 0:
  print("invalid number,YOU LOSE")
elif ai == 1:
  print(rock)
elif ai == 2:
  print(paper)
elif ai == 3:
  print(scissors)


if choice == 1 and ai == 2:
  print("you lose")
elif choice == 1 and ai == 3:
  print("you win")
elif choice ==2 and ai == 1:
  print("you won")
elif choice == 2 and ai == 3:
  print("you lose")
elif choice == 3 and ai == 1:
  print("you lose")
elif choice == 3 and ai == 2:
  print("you win")
elif choice == ai:
  print("draw")