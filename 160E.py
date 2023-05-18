lst = list(map(int,input("Write a list of numbers: ").split()))
num = int(input("Write a final number: "))

def hash_set(lst1, num1):
    for i in range(len(lst1)):
        for j in range(i,len(lst1)):
            if lst1[i] + lst1[j] == num1:
                print(f"[{lst1[i]} and {lst1[j]}]", end=" ")
def binar_look(lst2,num2):
    for i in range(len(lst2)):
        pair_num = lst2[i] - num2
        work_lst = lst2
        for j in range(i,len(lst2)):
            if work_lst[(int(len(work_lst))/2).round()] > pair_num:
                work_lst = work_lst[0,(int(len(work_lst))/2).round()]
            if work_lst[0] == pair_num:
                print(pair_num, num2)



how = input("How should we search? \n 1. Hash \n 2. Binar \n ")
if how == "1":
    hash_set(lst, num)
elif how == "2":
    binar_look(lst,num)

