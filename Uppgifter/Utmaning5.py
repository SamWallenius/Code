import random

rätt = 0

for i in range(5):
    rng1 = random.randrange(1,10)
    rng2 = random.randrange(1,10)

    produkt = int(rng1*rng2)

    svar = int(input("Vad är " +str(rng1)+" gånger "+str(rng2)+"? "))
    if svar == produkt:
        print("Rätt!")
        rätt += 1
    else:
        print("Fel.")

print("Du fick "+str(rätt)+" ut av 5 frågor rätt.")