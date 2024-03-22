# -*- coding: utf-8 -*-
"""Revature_Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gs3kVxhf3MVZdp6QSL56vM9N1fBebMg2
"""

import random
def Random_num():
  x,y=1,101
  name=input()
  total_attempts=5
  play_again = True
  while play_again:
      guessing_random_number(x,y,total_attempts,name)
      your_answer = input("Do you want to play again? (yes/no): ").lower()
      play_again = your_answer == "yes"
  print("Thank you for Playing!")
def guessing_random_number(x,y,total_attempts,name):
  num=random.randint(x,y)
  print(f"Hello!you are thinking of a number between {x} and {y}")
  print(f"You have {total_attempts} Attempts total.All the best!")
  chances=0
  while chances<total_attempts:
    user=int(input("enter your number:"))
    chances+=1
    if user<num:
      print(" Your Guess is too low")
    elif user>num:
      print("Your Guess is too high")
    else:
      print(f"Congratulations!{name}. You guessed it correctly.")
      break
  else:
    print(f"Sorry!{name}, {num} is the actual number.Better luck next time ")
Random_num()