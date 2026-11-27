print("1. Översätt från Svenska till Rövarspråket")
print("2. Översätt från Rövarspråket till Svenska")
nummer = int(input("Skriv ett eller två: "))
konsonanter = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
extra = []

def translate(val, text):
    check = 0
    if val == 1:
        for c in text:
            char = c.lower()
            if char in konsonanter and not char in extra:
                extra.append(char)
                text = text.replace(c, c+"o"+char)
    if val == 2:
        for c in text:
            char = c.lower()
            try: 
                if char in konsonanter and char == text[check]:
                    lista = list(text)
                    if check == 0:
                        lista.pop(check+1)
                        lista.pop(check)
                    else:
                        lista.pop(check+1)
                        lista.pop(check+1)
                    text = str(lista).replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                    check += 2

            except:
                pass
                
    return text

main = translate(nummer,input("Skriv en text: "))

print(main)
