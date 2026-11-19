import tkinter as tk
from PIL import Image, ImageTk
import random
import tkinter.font as tfont
import os
from pynput.keyboard import Key , Listener , Controller
Keyboard = Controller()

bag = []
press = ""
string = ""
main = ""
typing = True

def on_press(key):
    global press, string, main, typing
    press = str(key)
    if len(press) == 3 and typing == True:
        string += press
        string = string.replace("'","")
        main.configure(text=string)
        if int(20/len(string)*20) > 20:
            main.configure(font=tfont.Font(family="Arial", size=20))
        else:
            main.configure(font=tfont.Font(family="Arial", size=int(20/len(string)*20)))
    if typing == True and press == "Key.enter":
        typing = False

def show():
    global typing, main
    if typing == False:
        main.configure(text=bag)
        if int(20/len(str(bag))) > 20:
            main.configure(font=tfont.Font(family="Arial", size=20))
        else:
            main.configure(font=tfont.Font(family="Arial", size=int(20/len(str(bag)))))
def find():
    global string, typing
    if typing == False:
        amount = bag.count(string)
        main.configure(text="Det finns "+str(amount)+" av "+string+" i påsen.")
        if int(10/(len(string)*20)) > 20:
            main.configure(font=tfont.Font(family="Arial", size=20))
        else:
            main.configure(font=tfont.Font(family="Arial", size=int(10/(len(string)*20))))

def save():
    global string, typing
    if typing == False:
        bag.append(string)
        string = ""
        typing = True
        main.configure(text="")

def exit():
    global typing
    if typing == False:
        os._exit(0)


root = tk.Tk()
root.title("Påsen")
root.configure(background="black")
root.geometry("400x400")

root.bind("v", lambda event: show())
root.bind("f", lambda event: find())
root.bind("s", lambda event: save())
root.bind("q", lambda event: exit())

text5 = tk.Label(root,font=tfont.Font(family="Arial", size=20),text="Skriv något sedan tryck enter:")
text5.pack(side=tk.TOP, pady=15)
text4 = tk.Label(root,font=tfont.Font(family="Arial", size=20),text="[Q] Avsluta programmet")
text4.pack(side=tk.BOTTOM, pady=5)
text3 = tk.Label(root,font=tfont.Font(family="Arial", size=20),text="[F] Leta i påsen")
text3.pack(side=tk.BOTTOM, pady=5)
text2 = tk.Label(root,font=tfont.Font(family="Arial", size=20),text="[S] Spara i påsen")
text2.pack(side=tk.BOTTOM, pady=5)
text1 = tk.Label(root,font=tfont.Font(family="Arial", size=20),text="[V] Visa innehållet i påsen")
text1.pack(side=tk.BOTTOM, pady=5)

main = tk.Label(root,font=tfont.Font(family="Arial", size=20),text=string)
main.pack(side=tk.BOTTOM, pady=50)

with Listener(on_press=on_press) as listener:
    root.mainloop()
    listener.join()