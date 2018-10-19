n = int(input())  # кол-во секунд
n = n % (24 * 60 * 60)
hours = n // (60 * 60)
minutes = (n % (60 * 60)) // 60
seconds = n - hours * 60 * 60 - minutes * 60

minutesRes = str(minutes // 10) + str(minutes % 10)
secondsRes = str(seconds // 10) + str(seconds % 10)

print(hours, minutesRes, secondsRes, sep=':')
