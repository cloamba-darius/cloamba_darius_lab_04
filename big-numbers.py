def citeste_numere():
    try:
        with open("numere.txt", "r") as f:
            numere = [linie.strip().lstrip("0") for linie in f]

            if len(numere) < 2:
                print("Eroare: Fișierul nu conține suficiente numere.")
                return [], []

            if len(numere[0]) > 200 or len(numere[1]) > 200:
                print("Eroare: Unul dintre numere depășește limita maximă de 200 de cifre.")
                return [], []

            numar1 = [int(digit) for digit in numere[0]]
            numar2 = [int(digit) for digit in numere[1]]
            
            if numar1 == []:
                numar1 = [0]
            if numar2 == []:
                numar2 = [0]

    except FileNotFoundError:
        print(f"Fisierul numere.txt nu exista.")
        return [], []

    return numar1, numar2

def adunare(x, y):

    xc = x.copy()
    yc = y.copy()
    
    while len(xc) > len(yc):
        yc.insert(0, 0)
    while len(xc) < len(yc):
        xc.insert(0, 0)

    a = 0
    adunat = []

    for i in range(len(xc)-1, -1, -1):
        c = xc[i] + yc[i] + a
        a = c // 10
        adunat.insert(0, c % 10)

    if a > 0:
        adunat.insert(0, a)

    return adunat

def inmultire(x, y):

    xc = x.copy()
    yc = y.copy()

    #print('\n')
    #print(xc)
    #print(yc)
    
    rezultate = []

    for i in range(len(xc)-1, -1, -1):
        r = []

        # inseram zero-urile sa formam coloanele
        for k in range(len(xc) - 1 - i):
            r.insert(0, 0)

        a = 0
        for j in range(len(yc)-1, -1, -1):
            c = xc[i] * yc[j] + a
            r.insert(0, c % 10)
            a = c // 10

        if a > 0:
            r.insert(0, a)

        rezultate.append(r)

    #print(rezultate)
    rez_final = []
    for nr in rezultate:
        rez_final = adunare(rez_final, nr)
        #print(rez_final)

    este_zero = True
    for digit in rez_final:
        if digit != 0:
            este_zero = False
    if este_zero:
        return [0]

    return rez_final

def afiseaza_nr_mare(nr):
    for digit in nr:
        print(digit, end="")
    
def main():
    x, y = citeste_numere()

    afiseaza_nr_mare(x)
    print(" + ", end="")
    afiseaza_nr_mare(y)
    print(" = ", end="")
    afiseaza_nr_mare(adunare(x, y))

    print()

    afiseaza_nr_mare(x)
    print(" * ", end="")
    afiseaza_nr_mare(y)
    print(" = ", end="")
    afiseaza_nr_mare(inmultire(x, y))

if __name__ == "__main__":
    main()
