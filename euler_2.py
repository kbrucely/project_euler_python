limit = 4000000
var1 = 0
var2 = 1
sum = 0
seq = 0

while seq < limit:
    seq = var1 + var2
    if seq % 2 == 0:
        sum = sum + seq
    var1 = var2
    var2 = seq

print (sum)
    
