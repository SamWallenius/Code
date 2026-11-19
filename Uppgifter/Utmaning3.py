import random

tal = int(input("Hur många tal?: "))
undre = int(input("Undre gräns: "))
övre = int(input("Övre gräns: "))

while tal > 0:
    lista = []
    if tal >= 5:
        tal -= 5
        for i in range(5):
            rng = random.randrange(undre,övre)
            lista.append(rng)
        print(lista)
    elif tal < 5:
        for i in range(tal):
            rng = random.randrange(undre,övre)
            lista.append(rng)
        print(lista)
        tal = 0
