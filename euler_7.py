def isPrime(test):
    for x in range(2,test):
        if test % x == 0:
            return False

    return True

count = 0
limit = 10001     #change this value to test which prime number we want
test = 2
lastPrime = 0

while count < limit:
    if isPrime(test):
        count = count + 1
        lastPrime = test
    test = test + 1

print lastPrime