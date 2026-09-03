import random
import tkinter as tk
import tkinter.font as tfont


rng1 = 0
rng2 = 0
rng3 = 0

rolling = False

def roll():
    global rolling

    if rolling == False:
        rolling = True
        spin(0)


def spin(count):
    global rng1, rng2, rng3

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
    global rolling
    rolling = False
    if rng1 == rng2 and rng2 == rng3:
        print(f"{rng1} {rng2} {rng3} You win!")
        label1.configure(background="green")
        label2.configure(background="green")
        label3.configure(background="green")

    elif rng2 == rng1 + 1 and rng3 == rng2 + 1:
        print(f"{rng1} {rng2} {rng3} You win!")
        label1.configure(background="green")
        label2.configure(background="green")
        label3.configure(background="green")

    elif rng1 == rng2 and not rng2 == rng3:
        print(f"{rng1} {rng2} {rng3} You lose.")
        label1.configure(background="red")
        label2.configure(background="red")
        label3.configure(background="red")

    else:
        print(f"{rng1} {rng2} {rng3} You lose.")
        label1.configure(background="red")
        label2.configure(background="red")
        label3.configure(background="red")


root = tk.Tk()
root.title("Slot Machine")
root.configure(background="black")
root.geometry("300x150")

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

root.mainloop()