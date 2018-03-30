# John Deady, 2018-03-30
# Fibonacci series
# Adapted from https://en.wikipedia.org/wiki/Fibonacci_number
# By definition, the first two numbers in the Fibonacci sequence are either 1 and 1, or 0 and 1.
# Depending on the chosen starting point of the sequence, and each subsequent number is the sum of the previous two.

def fib(n):                                # This function returns the nth Fibonacci number
  i = 0                                    # Let i = 0
  j = 1                                    # Let j = 1
  n -= 1                                   # Let n = n - 1

  while n >= 1:                            # While Loop. While n is greater to or equal to 1 we continue
    i, j = j, i + j                        # i will equal to j and j = i + j
    n -= 1                                 # n will return n less 1
  
  return i                                 # Return i

x = 24                                     # Test the function with the following value 24
ans = fib(x)                               # ans eqaul to the function of 24
print("Fibonacci number", x, "is", ans)    # Print



# John Deady
# A program that displays Fibonacci numbers using people's names.

def fib(n):                                # This function returns the nth Fibonacci number
  i = 0                                    # Let i = 0
  j = 1                                    # Let j = 1
  n -= 1                                   # Let n = n - 1

  while n >= 1:                            # While Loop. While n is greater to or equal to 1 we continue
    i, j = j, i + j                        # i will equal to j and j = i + j in loop
      n -= 1                               # Let n = n - 1

   return i                                # # Return i

name = "Deady"                             # Name = Deady
first = name[0]                            # First letter of Name
last = name[-1]                            # Last letter of Name

# ord() function in Python. 
# Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object
# Or the value of the byte when the argument is an 8-bit string. 
# Adapted from https://www.geeksforgeeks.org/ord-function-python/

firstno = ord(first)                       # ord() of D
lastno = ord(last)                         # ord() of Y
x = firstno + lastno                       # x eqauls to the addition of ord() of D and Y

ans = fib(x)                               # ans eqaul to the function of x                  
print("My surname is", name)               # Print surname Deady
print("The first letter", first, "is number", firstno)        # Print ord() of D
print("The last letter", last, "is number", lastno)           # Print ord() of Y
print("Fibonacci number", x, "is", ans)                       # Print Answer

