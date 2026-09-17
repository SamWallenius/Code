import random
import tkinter as tk

points = 0
roll = 0
rolling = False

def check():
  global rolling
  if rolling == False:
    rolling = True
    roll()


def roll():
    global rolled, points, rolling
    rolled = random.randrange(1,6)
    points += rolled
    button.configure(text="Du rullade en " + str(rolled) + "\n\nPoäng: " + str(points))
    if points == 21:
        button.configure(text="DU VINNER! \n\nDu fick exakt 21 poäng!")
    elif points > 21:
        button.configure(text="Du förlorar. \n\nDu fick " + str(points) + " poäng, \nvilket är mer än 21.")
    else:
        rolling = False


root = tk.Tk()
root.title("TärningsSpel")
root.configure(background="black")
root.geometry("150x150")

button = tk.Button(
    root,
    text="Kasta Tärning",
    command=check,
    height=12,
    width=24
)
button.place(relx=1.0, rely=1.0, anchor="se")
button.pack()

root.mainloop()