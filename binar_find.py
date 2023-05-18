import random

def add_ran_num(A):
    for i in range(random.randrange(1, 28)):
        A.append(random.randrange(1, 100))
    A = list(set(A))
    A.sort()
    return A

def binar_search(array, target):
    left = 0
    right = len(array)
    index = 0
    while left < right:
        index = (left + right) // 2
        if array[index] == target:
            return index
        else:
            if array[index] < target:
                left = index + 1
            else:
                right = index
    return -1

A = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
A = add_ran_num(A)
print(A)
target_number = int(input())
index = binar_search(A, target_number)
print(index)