a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
target = 3

seen = {}

for i in range(len(a)):
    if target-a[i] in seen:
        print([seen[target-a[i]], i])
    seen[a[i]] = i