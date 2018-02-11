# John Deady, 07.02.2018
# The Collatz Conjecture

var = input("Enter something:")

while x > 1:    

 if x % 2 == 0:
    x = x // 2  
    print(x)
 else:
    x = (3 * x) + 1   
    print(x)

    
