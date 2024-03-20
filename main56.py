def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

liczba = int(input("Podaj liczbę: "))
if czy_parzysta(liczba):
    print("Liczba jest parzysta.")
else:
    print("Liczba nie jest parzysta.")
