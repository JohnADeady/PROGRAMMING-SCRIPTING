# John Deady ,18-03-15
# Factorial of a Number
# Write a function calling it factorial() that takes a single input/argument which is a positive integer and returns its factorial.
# The factorial of a number is that number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# Find the factorial of 5,7 and 10.
# I used Khan Academy, Stackflow and Codementor to solve this.
# We use a defined function so then we can re-use this code for each integer 5,7 & 10. 

def factorial (i):                             # A defined function called factorial for i.         
    number = 1                                 # Let number equal to 1
    while i >= 1:                              # This is a while loop. While i is greater than or equal to one we continue so 
        number *= i                            # We are multiplying all the integers of i by num
        i -= 1                                 # We are going to take 1 off i every loop
    return number
    
print (" the factorial of number 5 is:" , factorial (5))
print (" the factorial of number 7 is:" , factorial (7))
print (" the factorial of number 10 is:" , factorial (10))
