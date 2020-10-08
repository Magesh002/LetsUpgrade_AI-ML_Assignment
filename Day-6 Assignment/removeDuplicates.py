s = map(int, input("Enter the number in 1 line by split with space: ").split())

r = []
[r.append(n) for n in s if n not in r]
print(' '.join(str(n) for n in r))