def divisible(x):
    numList = [20, 19, 18, 17, 16, 14, 13, 11]
    for i in numList:
        if x % i != 0:
            return False
    return True 

counter=2520
notDivisible=True

while notDivisible:
   if divisible(counter):
       notDivisible=False
   counter = counter + 20

print counter-20
        
    
