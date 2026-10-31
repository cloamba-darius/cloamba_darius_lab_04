def citire():
    while True:
        try:
            x = int(input("\n-> Introduceti un numar par > 2: "))
            if x % 2 == 0 and x > 2:
                 break
            else:
                 print("Introduceti un numar par strict mai mare decat 2!")
        except ValueError:
            print("Introduceti un numar intreg valid!")

    return x

def este_prim(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def main():
    x = citire()

    for i in range(2, x // 2 + 1):
        if este_prim(i):
            if este_prim(x-i):
                print(f'{x} = {i} + {x-i}')

    print("\n-> Cititi inca un numar? (Y = yes / orice alta tasta = exit)")
    i = input()
    if i == "Y":
        main()

if __name__ == "__main__":
	main()