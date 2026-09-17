import random
import tkinter as tk
import time

class player:
  def __init__(self, name):
    self.name = name

plr1 = player("Player 1")
points1 = 0
points2 = 0
roll1 = 0
roll2 = 0
rolling = False

def check():
  global rolling
  if rolling == False:
    rolling = True
    roll()


def roll():
  global roll1, roll2, points1, points2, rolling
  roll1 = random.randrange(1,6)
  roll2 = random.randrange(1,6)
  print("Player 1 rolled a",roll1)
  time.sleep(0.5)
  print("Player 2 rolled a",roll2)
  time.sleep(0.5)
  if roll1 > roll2:
    points1 += 1
    print("Player 1 gets one point!")
  elif roll2 > roll1:
    points2 += 1
    print("Player 2 gets one point!")
  elif roll1 == roll2:
    print("It's a tie! Nobody gets points.")

  time.sleep(0.5)

  if points1 < 5 and points2 < 5:
    print("Player 1:",points1,"Points")
    print("Player 2:",points2,"Points")
    time.sleep(0.5)
    rolling = False
  elif points1 >= 5:
    print("Player 1 Wins!")
    points1 = 0
    points2 = 0
    rolling = False
  elif points2 >= 5:
    print("Player 2 Wins!")
    points1 = 0
    points2 = 0
    rolling = False


root = tk.Tk()
root.title("Duell")
root.configure(background="black")
root.geometry("150x150")

button = tk.Button(
    root,
    text="Roll",
    command=check,
    height=12,
    width=24
)
button.place(relx=1.0, rely=1.0, anchor="se")
button.pack()

root.mainloop()