def merge_lists(a, b):
    i = 0
    j = 0
    output = []
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            output.append(a[i])
            i+=1
        else:
            output.append(b[j])
            j+=1

    for index in range(i, len(a)):
        output.append(a[index])

    for index in range(j, len(b)):
        output.append(b[index])
    return output

print(merge_lists([1, 2, 5, 6, 8], [3, 4, 10])==[1, 2, 3, 4, 5, 6, 8, 10])
print(merge_lists([0, 1, 2], [-3, -2, -1])==[-3, -2, -1, 0, 1, 2])
print(merge_lists([1], [2])==[1, 2])
print(merge_lists([0, 2], [1])==[0, 1, 2])
print(merge_lists([-1], [100])==[-1, 100])