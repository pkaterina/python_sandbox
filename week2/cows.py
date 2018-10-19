n = int(input())
p = n // 10
q = n % 10
if q == 1 and p != 1:
    print(n, 'korova')
elif (q == 2 or q == 3 or q == 4) and p != 1:
    print(n, 'korovy')
else:
    print(n, 'korov')
