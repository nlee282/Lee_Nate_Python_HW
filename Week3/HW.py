def find_max(lst):
    maximum = float("-inf")
    for num in lst:
        if num>maximum:
            maximum = num
    return maximum

def remove_duplicates(lst):
    seen = set()
    output = []
    for num in lst:
        if not num in seen:
            output.append(num)
            seen.add(num)
    return output

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)



print("Find Max test cases:")
print(find_max([1, 2, 3, 4])==4)
print(find_max([7, 1, 122])==122)
print(find_max([5, 2, 1234, 43214])==43214)
print(find_max([0])==0)
print(find_max([-1, -2, -3, -4, -5])==-1)


print("Remove Duplicates test cases:")
print(remove_duplicates([1, 1, 2, 3, 4])==[1, 2, 3, 4])
print(remove_duplicates([1, 1, 1, 1, 1, 1, 1])==[1])
print(remove_duplicates([-1, -1, -2, 0, 0, 2, 2, 2, 2])==[-1, -2, 0, 2])
print(remove_duplicates([5, 2, 2, 2, 5])==[5, 2])
print(remove_duplicates([12])==[12])

print("Factorial Cases")
print(factorial(0)==1)
print(factorial(1)==1)
print(factorial(2)==2)
print(factorial(3)==6)
print(factorial(4)==24)