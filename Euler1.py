# John Deady, 18-03-24
# Euler Problem 1
# Sum the multiples of 3 and 5 below 1000
# Adapted from https://projecteuler.net/problem=1

i = 1                                  # let i = 1 as your starting integer
sum = 0                                # let sum = 0 this is needed in order to sum multiplies

while i < 1000:                        # This is a while loop. We are looking for multiples of 3 and 5 below 1000.
 if (i % 3 == 0) or (i % 5 == 0):      # if statement. If i is divided by 3 or 5 and there is no remainder i.e. it's a even integer
    sum = sum + i                      # We add all the multiples of 3 and 5 together
 i = i + 1                             # We will add 1 to i until we get to 1000

print("Sum of the multiplies of 3 and 5:", sum) # This will print the sum of the multiples of 3 and 5

