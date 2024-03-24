a = [10, 20, 30, 40]
b = [50, 60, 70]

for i in range(len(a) - 1, -1, -1):
    print(f"{i}: {a[i]}", end=' ')
print()

for i in reversed(range(0, len(a))):
    print(f"{i}: {a[i]}", end=' ')
print()




c = [(10, '10'), (5, '5')]
print(sorted(c, key=lambda x: x[0]))
