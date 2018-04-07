#John Deady, 2018-23-02
#Dice Rolling Simulator

# Adapted from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# The Goal: this program involves writing a program that simulates a rolling dice. 
# When the program runs, it will randomly choose a number between 1 and 6.   
# It should then ask you if you’d like to roll again.
# For this project, you’ll need to set the min and max number that your dice can produce i.e minimum of 1 and a maximum of 6.
# You’ll also want a function that randomly grabs a number within that range and prints it.
# The references I used to solve this problem were from Stackflow and Codecademy.

from random import randint                          # Randint is a function that is part of the random module.
print(randint(1,6),"Would you like to roll again")  # Randint will pull a random number between 1 and 6.
                                                    # It will then ask, would you like to roll again.
