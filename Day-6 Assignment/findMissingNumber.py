s = set(input("Enter the number in 1 line by split with space: ").split())

for i in range(1, len(s)):
    if str(i) not in s:
        print(i)
        break
