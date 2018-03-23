# John Deady, 2018-04-03
# Sum square difference


a = 0
b = 0
    
for i in range (1,101):
    b += i
    a += i**2

n = b**2 - a
print (n)


