# John Deady ,18-03-15
# Factorial of a Number
# Write a function calling it factorial() that takes a single input/argument which is a positive integer and returns its factorial.
# The factorial of a number is that number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# Find the factorial of 5,7 and 10.
# I used Khan Academy, Stackflow and Codementor to solve this.
# We use a defined function so then we can re-use this code for each integer 5,7 & 10. 
# Recursive Factorial Function - Using the function in the code

def factorial (i):                             # A defined function called factorial for i.         
    if n <= 1:                                 # If n is greater or equal to one we will get a result of one
        return 1                               # Return 1
    else:                                      # If not greater or equal to one
        n = n * factorial(n - 1)               # We multiply n by itself and function itself less n minus 1 [ie if i = 2 n = 2 * (2-1)]
    return n   
    
print (" the factorial of number 5 is:" , factorial (5))
print (" the factorial of number 7 is:" , factorial (7))
print (" the factorial of number 10 is:" , factorial (10))
