i = 1
x = 1
N = int(input())
lst = []
for L in range(N):
    while x != i:
        if i%x == 0:
            lst.append(x)
        x += 1
    if sum(lst) == i:
        print(f"{i} - liczba doskonała")
        print(f"{lst} - dzielniki liczby {i}, \nа [{sum(lst)}] - suma dzielników liczby {i}, oprócz niego samego.\n")
    if i == x:
        i += 1
        x = 1
        lst = []