import tkinter as tk
from PIL import Image, ImageTk
import random
from pynput.keyboard import Key , Listener , Controller
import os
import sys
import tkinter.font as tfont
easywords = [
    "katt", "hund", "bil", "bok", "hus", "sol", "mat", "glas", "fisk", "träd",
    "blomma", "stol", "bord", "lampa", "skola", "vatten", "fågel", "mjölk", "bröd", "äpple",
    "klocka", "penna", "papper", "vante", "mamma", "pappa", "barn", "vän", "cykel", "dator",
    "telefon", "skog", "gräs", "himmel", "stjärna"
]
mediumwords = [
    "apelsin", "banan", "citron", "fjäril", "giraff", "hästsko", "insekter", "jordgubbe", "kanot", "lejon",
    "motorcykel", "nyckelpiga", "ormbunke", "pingvin", "rymdraket", "solros", "timglas", "utsikt", "varg", "xylofon",
    "yxa", "zebra", "ananas", "ballong", "choklad", "dinosaurie", "ekorre", "flygplan", "gitarr", "helikopter",
    "isbjörn", "jojo", "känguru", "linjal", "musiker"
]
hardwords = [
    "jazz", "buzz", "fenix", "kafé", "cello", "psykolog", "schysst", "strix", "vajer", "galaxy",
    "kvarts", "zloty", "djungel", "kitsch", "inoxa", "limousin", "oas", "fest", "pyjamas", "quiz",
    "razzia", "sfinx", "tsunami", "uti", "valp", "whisky", "xenon", "yoghurt", "zink", "äventyrlig"
]
presses = []
presses2 = []
Keyboard = Controller()
folder = sys.path[0]
diff = "medium"
started = False
word = "none"
press = "n"
length = 4
text1 = None
text2 = None
panel = None
wordtext = "----"
lives = 7

def start():
    global started, text1, text2, length, word, wordtext
    started = True
    length = int(len(word))
    button1.destroy()
    button2.destroy()
    button3.destroy()
    text1 = tk.Label(root,font=tfont.Font(family="Arial", size=30),text="Guess a letter!")
    text1.pack(side=tk.BOTTOM, pady=20)

    wordtext = "-"*length
    text2 = tk.Label(root,font=tfont.Font(family="Arial", size=15),text=wordtext)
    text2.pack(side=tk.TOP, pady=20)

def easy():
    global diff, word, easywords
    diff = "easy"
    word = random.choice(easywords)
    start()

def medium():
    global diff, word, mediumwords
    diff = "medium"
    word = random.choice(mediumwords)
    start()

def hard():
    global diff, word, hardwords
    diff = "hard"
    word = random.choice(hardwords)
    start()

def on_press(key):
    global started, press, length, text1, text2, wordtext, presses, presses2, panel, lives
    press = str(key)
    if started == True and len(press) <= 3:
        if press in presses or press in presses2:
            return
        elif not press in presses and not press in presses2:
            found = False
            pos = 0
            for char in word:
                if "'"+char.lower()+"'" == press.lower():
                    presses2.append(press)
                    wordtext = wordtext[:pos] + char + wordtext[pos+1:]
                    text2.configure(text=wordtext)
                    found = True
                    if not "-" in wordtext:
                        started = False
                        text1.configure(text="Du Vinner!", font=tfont.Font(family="Arial", size=30))
                pos += 1
            
            if found == False:
                presses.append(press)
                text1.configure(text=presses, font=tfont.Font(family="Arial", size=int(100/(len(presses)))+4))
                lives -= 1
                try: img = ImageTk.PhotoImage(Image.open(folder+"/Gubbe"+str(lives)+".jpg")) 
                except:
                    return
                else:
                    panel.configure(image=img)
                    panel.photo = img

                if lives == 0:
                    started = False
                    text1.configure(text="Du Förlorar.", font=tfont.Font(family="Arial", size=30))
                    text2.configure(text="Ordet var "+word+".")

root = tk.Tk()
root.title("Hangman")
root.configure(background="black")
root.geometry("400x400")
img = ImageTk.PhotoImage(Image.open(folder+"/Gubbe7.jpg"))
panel = tk.Label(root, image = img, width=10000, height=10000)
panel.pack()
panel.place(relx=0.5, rely=0.35, anchor="center")

button1 = tk.Button(
    root,
    text="Lätt",
    command=easy,
    height=6,
    width=12
)
button1.pack()
button1.place(relx=0.2, rely=0.75, anchor="center")

button2 = tk.Button(
    root,
    text="Medium",
    command=medium,
    height=6,
    width=12
)
button2.pack()
button2.place(relx=0.5, rely=0.75, anchor="center")

button3 = tk.Button(
    root,
    text="Svårt",
    command=hard,
    height=6,
    width=12
)
button3.pack()
button3.place(relx=0.8, rely=0.75, anchor="center")

with Listener(on_press=on_press) as listener:
    root.mainloop()
    listener.join()