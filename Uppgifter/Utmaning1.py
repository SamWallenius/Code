import random


for i in range(3):
    förnamn = ["Wilmer","Gerbert","John","Elias","Nils","Pablo","Josefin","Freja","Ester","Jack"]
    efternamn = ["Nordborg", "Örnkvist", "Broström", "Strömkvist", "Nordin", "Lund", "Sandström", "Åberg", "Falk", "Andersson"]


    choose1 = random.choice(förnamn)
    choose2 = random.choice(efternamn)


    namn = choose1+" "+choose2
    print(namn)
