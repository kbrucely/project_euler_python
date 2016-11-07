end = 1000
sum = 0

for a in range (1, end):
    if a % 3 == 0:
        sum = sum + a
    elif a % 5 == 0:
        sum = sum + a

print (sum)
