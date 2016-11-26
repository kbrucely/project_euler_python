import math

def isPrime ( x ):
    for i in xrange ( 2, x):
        if (x % i == 0):
            return False

    return True

test = 13195
#test = 600851475143
largest = 0

for x in xrange (2, test):
    if isPrime(x):
        if test % x == 0:
            largest = x

print (largest)
