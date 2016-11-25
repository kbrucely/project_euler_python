def isPrime ( x ):
    for i in range ( 2, x):
        if (x % i == 0):
            return False

    return True


test = 13195
largest = 0

for x in range (2, test):
    if test % x == 0 and isPrime(x):
        largest = x

print (largest)
