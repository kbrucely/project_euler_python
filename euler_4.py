def isPalindrome(x):
    mystr = str(x)
    revstr = mystr[::-1]
    if mystr == revstr:
        return True
    else:
        return False

x=100
y=100
largest=0

while x <= 999:
    while y <= 999:
        if isPalindrome(x*y) and x*y > largest:
            largest = x*y
        y=y+1
    y=100
    x=x+1

print largest 

