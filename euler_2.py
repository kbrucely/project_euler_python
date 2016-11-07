limit = 4000000
var1 = 0
var2 = 1
sum = 0

for i in range (1, limit):
    seq = var1 + var2
    if seq % 2 == 0:
        sum = sum + seq
    next  = var1 + var2
    var1 = var2
    var2 = next

print (sum)
    
