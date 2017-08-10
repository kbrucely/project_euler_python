limit = 10
limit = limit + 1

sumSquares = 0
squareSums = 0

for x in xrange (1, limit):
    sumSquares = sumSquares + (x*x)
    squareSums = squareSums + x

squareSums = squareSums * squareSums
difference = squareSums - sumSquares

print difference