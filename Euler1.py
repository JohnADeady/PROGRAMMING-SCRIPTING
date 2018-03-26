# John Deady, 18-03-24
# Euler Problem 1
# Sum the multiples of 3 and 5 below 1000
# Adapted from https://projecteuler.net/problem=1

i = 1                                  # let i = 1 as your starting integer
sum = 0                                # let sum = 0 this is needed in order to sum multiplies

while i < 1000:                        
 if (i % 3 == 0) or (i % 5 == 0):
    sum = sum + i
 i = i + 1 

print("Sum of the multiplies of 3 and 5:", sum)

