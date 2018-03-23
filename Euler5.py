# John Deady, 2018-23-02
# Euler Project Smallest Number 

# Adapted from https://projecteuler.net/problem=5

# I have a range of 1 to 20. Find the smallest number that 
# all can evenly be divide into it.

primes = [2,3,5,7,11,13,17,19]
x = 1 
for p in primes:
    n = 2
    x *= p
    while (p**n < 21):
        x *= p
        n += 1

print (x)

