# John Deady, 07.02.2018
# The Collatz Conjecture - Exercise 3
# (A) Write a single Python script that starts with an integer. 
# (B) And repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd). 
# (C) Using a while loop and if statement.
# In order to understand the problem I used the website  https://en.wikipedia.org/wiki/Collatz_conjecture
# To find a solution, my main port of call was stackflow.
# I divided the problem into 3 parts in order to find a solution: variable input, even number part (divide) and odd number part (multiply).


var = input("Enter something:")   # You will be asked to enter a number of your choice when code is ran

while x > 1:                      # This is the while loop. This will run until x is greater than 1. We are looking for 1

 if x % 2 == 0:                   # This is an if statement. When x is divided by 2 there is no remainder i.e. it is even
    x = x // 2                    # If x is even this is divide by 2
    print(x)                      # Prints the result for x
 else:                            # This is else. Meaning if not an even number then it must be odd
    x = 3x + 1                    # If odd then the code multiplies by 3 and adds 1
    print(x)                      # Prints the result for x

    
