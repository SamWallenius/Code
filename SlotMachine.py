import random
import tkinter as tk
import tkinter.font as tfont
from pynput.keyboard import Key , Listener , Controller
Keyboard = Controller()

bet = 1
budget = 100
rng1 = 0
rng2 = 0
rng3 = 0

rolling = False

def roll():
    global rolling, budget, bet

    if rolling == False and budget >= bet:
        rolling = True
        budget -= bet
        money.configure(text=budget)
        spin(0)


def spin(count):
    global rng1, rng2, rng3, budget, bet

    label1.configure(background="white")
    label2.configure(background="white")
    label3.configure(background="white")

    if count < 40:
        rng1 = random.randrange(1, 10)
        label1.configure(text=rng1)

    if count < 80:
        rng2 = random.randrange(1, 10)
        label2.configure(text=rng2)

    if count < 120:
        rng3 = random.randrange(1, 10)
        label3.configure(text=rng3)

    if count < 120:
        root.after(3, spin, count + 1)
    else:
        check()


def check():
    global rolling, budget, bet
    rolling = False
    if rng1 == rng2 and rng2 == rng3:
        if not rng1 == 6 and not rng1 == 7:
            label1.configure(background="green")
            label2.configure(background="green")
            label3.configure(background="green")
            budget += bet * 50
            money.configure(text=budget)
    
    elif rng1 == 6 and rng2 == 6 and rng3 == 6:
        label1.configure(background="red4")
        label2.configure(background="red4")
        label3.configure(background="red4")
        budget = round(budget / 666)
        money.configure(text=budget)

    elif rng1 == 7 and rng2 == 7 and rng3 == 7:
        label1.configure(background="goldenrod")
        label2.configure(background="goldenrod")
        label3.configure(background="goldenrod")
        budget += bet * 777
        money.configure(text=budget)

    elif rng2 == rng1 + 1 and rng3 == rng2 + 1:
        if not rng1 == 1:
            label1.configure(background="green yellow")
            label2.configure(background="green yellow")
            label3.configure(background="green yellow")
            budget += bet * 10
            money.configure(text=budget)

    elif rng1 == 1 and rng2 == 2 and rng3 == 3:
        label1.configure(background="green")
        label2.configure(background="green")
        label3.configure(background="green")
        budget += bet * 123
        money.configure(text=budget)

    elif rng2 == rng1 - 1 and rng3 == rng2 - 1:
        label1.configure(background="green yellow")
        label2.configure(background="green yellow")
        label3.configure(background="green yellow")
        budget += bet * 10
        money.configure(text=budget)

    elif rng1 == rng2 and not rng2 == rng3:
        label1.configure(background="yellow")
        label2.configure(background="yellow")
        label3.configure(background="yellow")
        budget += bet * 5
        money.configure(text=budget)

    elif rng2 == rng3 and not rng1 == rng2:
        label1.configure(background="yellow")
        label2.configure(background="yellow")
        label3.configure(background="yellow")
        budget += bet * 5
        money.configure(text=budget)

    elif rng1 == rng3 and not rng1 == rng2:
        label1.configure(background="orange")
        label2.configure(background="orange")
        label3.configure(background="orange")
        budget += bet * 2
        money.configure(text=budget)

    else:
        label1.configure(background="red")
        label2.configure(background="red")
        label3.configure(background="red")
        budget += round(bet / 4)
        money.configure(text=budget)

    if budget <= 0:
        budget = 1
        money.configure(text=budget)
    if bet > budget:
        bet = budget
        betchange = "Bet:",bet
        bettext.configure(text=betchange)

def on_press(key):
    global bet
    try:
        if key == key.up and bet < budget:
            bet = bet + 1
            betchange = "Bet:",bet
            bettext.configure(text=betchange)
        elif key == key.down and bet > 1:
            bet = bet - 1
            betchange = "Bet:",bet
            bettext.configure(text=betchange)
        elif key == key.right and bet * 2 < budget:
            bet = bet * 2
            betchange = "Bet:",bet
            bettext.configure(text=betchange)
        elif key == key.right and bet * 2 > budget:
            bet = budget
            betchange = "Bet:",bet
            bettext.configure(text=betchange)
        elif key == key.left and bet > 1:
            bet = round(bet / 2)
            betchange = "Bet:",bet
            bettext.configure(text=betchange)
        if bet <= 0:
            bet = 1
            betchange = "Bet:",bet
            bettext.configure(text=betchange)
    except AttributeError:
        pass

root = tk.Tk()
root.title("Slot Machine")
root.configure(background="black")
root.geometry("1000x150")

textfont = tfont.Font(family="Arial", size=80)

label1 = tk.Label(root, text="0", font=textfont, bg="white")
label1.pack(side=tk.LEFT, pady=20)

label2 = tk.Label(root, text="0", font=textfont, bg="white")
label2.pack(side=tk.LEFT, pady=20)

label3 = tk.Label(root, text="0", font=textfont, bg="white")
label3.pack(side=tk.LEFT, pady=20)

button = tk.Button(
    root,
    text="ROLL",
    command=roll,
    height=6,
    width=12
)
button.place(relx=1.0, rely=1.0, anchor="se")
button.pack(side=tk.LEFT, pady=20)

money = tk.Label(root, text="100", font=textfont, bg="black", fg="green")
money.pack(side=tk.LEFT, pady=20)
moneytext = tk.Label(root, text="$", font=textfont, bg="black", fg="green")
moneytext.pack(side=tk.LEFT, pady=20)

bettext = tk.Label(root,font=textfont,text="Bet: 1")
bettext.pack(side=tk.RIGHT, pady=20)

with Listener(on_press=on_press) as listener:
    root.mainloop()
    listener.join()