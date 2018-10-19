prev = int(input())
next = prev
count = 0
if prev != 0:
    count = 1
countMax = 0
while next != 0:
    next = int(input())
    if next != prev:
        if count > countMax:
            countMax = count
        count = 1
    if next == prev:
        count += 1
    prev = next
print(countMax)
