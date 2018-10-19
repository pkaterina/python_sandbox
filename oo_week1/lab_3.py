n = input()
aset = set(n)
c = [int(i) for i in aset]
c.sort()
print(tuple(c))
c.reverse()
print(tuple(c))
