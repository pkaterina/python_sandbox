h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

allSec1 = h1 * 60 * 60 + m1 * 60 + s1
allSec2 = h2 * 60 * 60 + m2 * 60 + s2

print(allSec2 - allSec1)
