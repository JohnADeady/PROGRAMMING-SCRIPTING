#John Deady, 2018-23-02
# Guess the Number

# Adapted from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

from random import randint

target = randint(1,10)
guess = 11


print ("Guess a number between 1 and 10")
while guess != target:
  guess = int(input("Please enter your guess:"))    
  if guess == target:
      print (guess,"Yahoo")
  elif guess < target:
      print ("Too low")
  else:
      print ("Too high")  
  
