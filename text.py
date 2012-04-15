print("Zadavejte cisla \n")

cislo = 0
soucet = 0

while True:
    cislo = input("cislo: ")
    if cislo:
        try:
            number = int(cislo)
        except ValueError as err:
            print(err)
            continue
        soucet += number
    else:
        break
    
print("Celkovy soucet: ", soucet)
        s