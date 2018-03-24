#John Deady, 2018-23-02
# Guess the Number

# Adapted from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# The program will first randomly generate a number unknown to the user.The user needs to guess what that number is.
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong.
# If the user guesses correctly, a positive indication should appear.
# My main resource in solving this problem was Stackflow,pythonforbeginners and Codecademy.
# I brokedown the solution into a number of parts in order to solve this: random integer, if equal print.., and if too low/high print.. 


from random import randint                 # We want to generate a random integer -Randiant function accepts two parametes high and low


x = randint(1,10)                          # Our two parameters are between 1 (lowest) and 10 (highest)
guess = 11                                 # Guess will be equal to 11


print ("Guess a number between 1 and 10")  # When code is ran it will ask for guess between 1 and 10
while guess != x:                          # This is a while loop. While guess is not equal to x continue the loop.
  guess = int(input("Please enter your guess:"))    # It will also ask you to enter your guess which will be between 1 and 10.
  if guess == x:                           # If your guess is equal to the random number generated. You will be correct
      print (guess,"Yahoo Correct")        # And correct will generate the number guessed plus statement ' Yahoo Correct'
  elif guess < x:                          # If your guess is less than the number generated then your incorrect.      
      print ("Too low, Try again")         # Incorrect will state ' Too low, Try again'
  else:                                    # Else statement means if it is not equal or less than numbered generated it will be too high.
      print ("Too high, Try again")        # It too high it will print 'Too high, Try again'
  
