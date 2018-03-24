# John Deady, 2018-25-02
# Euler Problem 3 - Largest Prime Factor.
# To understand what a prime number was I used http://planetmath.org/howtofindwhetheragivennumberisprimeornot
# This problem was adapted from https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143 ?
# In order to find the solution to this problem I used Stackflow.
 
n = 600851475143                 # I let n equal to the our starting integer. We needed to find the largest prime number of this integer.
i = 2                            # i was our starting prime number.
while i * i < n:                 # This is a while loop. This piece of code states while i multiply by i is less than N we continue
     while n % i == 0:           # This while loop states while n divided by i is equal to zero we continue
         n = n // i              # If the two while loops are satisfied then n would be divided by i 
     i = i + 1                   # We keep increasing i by 1 until we get our solution

print (n)                        # Once the above criteria is satisfied print n
