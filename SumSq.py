# John Deady, 2018-04-03
# Euler Problem 6 - Sum Square Differences

# Adapted from https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# In order to find a solution to this problem I used Project Euler and Stackflow.
# I divided this problem into 3 parts: sum of the squares , square of the sum and subtracting one from the other.

a = 0                      # We let a equal to zero as our starting integer for sum of the squares
b = 0                      # We let b equal to zero as our starting integer for square of the sum
    
for i in range (1,101):    # i is our range for 1 to 100 so our end point is 101 in order to finish at 100
    b += i                 # b equals to the sum of the range i 
    a += i**2              # a equals to the square of the sum of i 

n = b**2 - a               # n is equal to square of b less a 
print (n)                  # This is will print n i.e. you answer


