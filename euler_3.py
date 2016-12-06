import math

def isPrime ( x ):
    for i in xrange ( 2, x):
        if (x % i == 0):
            return False

    return True

#test = 13195
test = 600851475143
largest = 0

#it is very important to check first if a number is a factor and then if it's prime and not the other way around.  the first way takes weeks.  
for x in xrange (2, int(math.floor(math.sqrt(test)))):
    if test % x == 0:
        if isPrime(x):
            largest = x

print (largest)
