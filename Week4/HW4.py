a = [1, 2, 5, 6, 8]
b = [3, 4, 10]
output = []
i = 0
while i<len(a):
    if a[i]<b[0]:
        output.append(a[i])
    elif a[i]>b[0] and len(b)>0:
        output.append(b[0])
        b.remove(b[0])
    i += 1
print(output)