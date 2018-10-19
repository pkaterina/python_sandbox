x = int(input())
y = int(input())

d = 1
while x < y:
    d = d + 1
    x = x + 0.1 * x
print(d)
