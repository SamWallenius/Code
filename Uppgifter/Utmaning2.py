import random


personer = []
person = input("Skriv namn: ").split()
lag1 = []
lag2 = []


for i in person:
    rng = random.randrange(1,2)
    if rng == 1:
        if len(lag1) <= len(lag2):
            lag1.append(i)
        else:
            lag2.append(i)
    if rng == 2:
        if len(lag2) <= len(lag1):
            lag2.append(i)
        else:
            lag1.append(i)


print("Lag 1 är:",lag1)
print("Lag 2 är:",lag2)
