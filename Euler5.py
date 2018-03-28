# John Deady, 2018-23-02
# Euler Project Smallest Number 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Adapted from https://projecteuler.net/problem=5
# I have used stackflow in order to solve this problem. 
# We take prime numbers only. Integers (6,8,9,10,12,15,20) are divisibles by 2,3 and 5.
# We multiply all the prime numbers together to get 9,699,690
# Then

primes = [2,3,5,7,11,13,17,19]          # Let primes equal to the prime numbers up to 20.
x = 1                                   # Let x = 1
for p in primes:                        # for statemtent. P equals to primes.
    n = 2                               # Let n = 2
    x *= p                              # x is equal to x multiply p (i.e.2*3*5*7*11*17*19)
    while (p**n < 21):                  # This is a while loop. This while loop states p to the power of n is less than 21.
        x *= p                          # x is equal to x multiply p
        n += 1                          # We continue adding 1 to n until 20.

print (x)                               # Print x (The smallest positive number)

