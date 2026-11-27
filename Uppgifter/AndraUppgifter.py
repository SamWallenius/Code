import random
hp1 = 100
hp2 = 100

def status():
    print("Spelare:",hp1,"HP")
    print("Monster:",hp2,"HP")

def menu():
    print("-----------------")
    print("1. Svärdshugg")
    print("2. Eldklot")
    print("3. Läkande dryck")
    print("4. Livsstjälande Stråle")
    print("-----------------")

def pt(val):
    global hp1, hp2
    if val == 1:
        dmg = random.randint(15,25)
        miss = random.randint(1,30)
        print("-----------------")
        if miss > 3:
            hp2 -=  dmg
            print("Du högg monstret med svärdet och gjorde",dmg,"skada.")
        elif miss > 1 and miss <= 3:
            print("Du försökte att hugga monstret men missade.")
        elif miss == 1:
            dmg = random.randint(10,20)
            hp1 -=  dmg
            print("Du tappade svärdet och skar dig själv vilket gjorde",dmg,"skada.")
        print("-----------------")

    if val == 2:
        dmg = random.randint(25,35)
        miss = random.randint(1,15)
        print("-----------------")
        if miss > 3:
            hp2 -=  dmg
            print("Eldklotet träffade monstret för",dmg,"skada.")
        elif miss > 1 and miss <= 3:
            print("Du missade monstret med eldklotet.")
        elif miss == 1:
            dmg = random.randint(25,35)
            hp1 -=  dmg
            print("Du misslyckades med trollformeln vilket fick dig att explodera och ta",dmg,"skada.")
        print("-----------------")

    if val == 3:
        dmg = random.randint(17,22)
        miss = random.randint(1,20)
        print("-----------------")
        if miss > 3:
            if hp1 + dmg > 100:
                hp1 = 100
                print("Du drack den läkande drycken och fick fullt HP")
            else:
                hp1 +=  dmg
                print("Du drack den läkande drycken och fick tillbaka",dmg,"HP.")
        elif miss > 1 and miss <= 3:
            print("Tappade flaskan och den sprack i bitar.")
        elif miss == 1:
            dmg = random.randint(5,10)
            print("Du tappade flaskan på din fot och skar dig på glasbitarna, du tog",dmg,"skada.")
        print("-----------------")

    if val == 4:
        dmg = random.randint(5,10)
        miss = random.randint(1,20)
        print("-----------------")
        if miss > 5:
            hp2 -= dmg
            if hp1 + dmg > 100:
                hp1 = 100
                print("Du träffade strålen, den gjorde",dmg,"skada och gav dig fullt hp.")
            else:
                hp1 +=  dmg
                print("Du träffade strålen och stal",dmg,"HP från monstret.")
        elif miss > 2 and miss <= 5:
            hp2 -= dmg
            print("Montret blev träffat av strålen och tog",dmg,"skada, men du lyckades inte dra ut liv ur den.")
        elif miss <= 2:
            print("Strålen missade helt.")
        print("-----------------")

def mt():
    global hp1, hp2
    dmg = random.randint(10,25)
    hp1 -= dmg
    print("-----------------")
    print("Monstret klöste dig vilket gjorde",dmg,"skada.")
    print("-----------------")

while hp1 > 0 and hp2 > 0:
    if hp1 and hp2 > 0:
        status()
        menu()
        choice = int(input("Välj vad du vill göra med ett nummer: "))
        pt(choice)
        if hp1 and hp2 > 0:
            status()
            input("Tryck Enter för att fortsätta: ")
    if hp1 and hp2 > 0:
        mt()
        if hp1 and hp2 > 0:
            status()
            input("Tryck Enter för att fortsätta: ")

if hp2 <= 0 and hp1 > 0:
    print("Du vann med",hp1,"HP kvar!")
elif hp1 <= 0 and hp2 > 0:
    print("Monstret besegrade dig, det hade",hp2,"HP kvar.")
elif hp1 <= 0 and hp2 <= 0:
    print("Det blev lika, ni dog samtidigt!")