a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())

if c < b:
    (b, c) = (c, b)
if b < a:
    (a, b) = (b, a)
if c < b:
    (b, c) = (c, b)

if e < d:
    (e, d) = (d, e)

if a <= d and b <= e or b <= e and c <= d:
    print('YES')
else:
    print('NO')
