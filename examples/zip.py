# References:
#
#   [1] https://docs.python.org/2/library/functions.html#zip

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

zippedXY = zip(x, y)
print zippedXY
for a, b in zippedXY:
  print "a = ", a, " b = ", b

zippedXYZ = zip(x, y, z)
print zippedXYZ
for a, b, c in zippedXYZ:
  print "a = ", a, " b = ", b, " c = ", c
