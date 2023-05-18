def alg1(n):
    cnt = 1
    i = 2
    lst = []
    while cnt < n/2+1:
        lst.append(i)
        cnt += 1
        i += 4
        lst.append(i)
        i -= 3
    print(lst)
    print(lst[n-1])
def alg2(n):
    lst = []
    num = -2
    pl_min = - 1
    for i in range(n-1):
        num = abs(num)+3
        pl_min *= -1
        num *= pl_min
    print(num)
def alg3(n):
    lst = [1,2,-4]
    for i in range(2, n-1):
        lst.append(lst[i-2] - abs(lst[i]))
    print(lst)
# 1 2 -4 -3 -1 -5 -8 -9 -14
alg3(int(input()))