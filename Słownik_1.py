dict = {0:"owo",1:"hehe"}
i = 0
m = len(dict)

while True:
    print("""1. Dodać do słownika
2. Usuwać wybrane definicje  
3. Szukać definicji
4. Skończyć""")
    i = input()
    if i == "1":
        inf = input("Co dodać? ")
        dict.update({m:inf})
        m += 1
        inf == ""
        print(dict)
    if i == "2":
        key = int(input("Podaj klucz "))
        del(dict[key])
        print(dict)
    if i == "3":
        inf = input("Co szukać? ")
        print(dict)
        if inf in dict.values():
            indx = list(dict.values())
            ans = f"Tak, indeks - {indx.index(inf)}"
        print(ans)
    if i == "4":
        break
print(dict)