import tkinter as tk
from PIL import Image, ImageTk
from keyboard import on_press
import keyboard

x = 0.5
y = 0.5

root = tk.Tk()
root.title("WawaGame")
root.configure(background="black")
root.geometry("1000x1000")
root.attributes("-fullscreen", True)
img = ImageTk.PhotoImage(Image.open("C:/Users/sam.wallenius/Documents/WawaGame/WawaMan.png"))
panel = tk.Label(root, image = img, width=25, height=25)
panel.pack()
panel.place(relx=x, rely=y, anchor="center")

while True:
    try:
        if keyboard.is_pressed("w") and not keyboard.is_pressed("s") and not keyboard.is_pressed("a") and not keyboard.is_pressed("d") and y > 0.005:
            y = y - 0.002
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("s") and not keyboard.is_pressed("w") and not keyboard.is_pressed("a") and not keyboard.is_pressed("d") and y < 0.995:
            y = y + 0.002
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("a") and not keyboard.is_pressed("d") and not keyboard.is_pressed("w") and not keyboard.is_pressed("s") and x > 0.0025:
            x = x - 0.0015
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("d") and not keyboard.is_pressed("a") and not keyboard.is_pressed("w") and not keyboard.is_pressed("s") and x < 0.9975:
            x = x + 0.0015
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("d") and keyboard.is_pressed("w") and not keyboard.is_pressed("s") and not keyboard.is_pressed("a") and x < 0.9975 and y > 0.005:
            x = x + 0.0015 * 0.7
            y = y - 0.002 * 0.7
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("d") and keyboard.is_pressed("s") and not keyboard.is_pressed("w") and not keyboard.is_pressed("a") and x < 0.9975 and y < 0.995:
            x = x + 0.0015 * 0.7
            y = y + 0.002 * 0.7
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("a") and keyboard.is_pressed("w") and not keyboard.is_pressed("s") and not keyboard.is_pressed("d") and x > 0.0025 and y > 0.005:
            x = x - 0.0015 * 0.7
            y = y - 0.002 * 0.7
            panel.place(relx=x, rely=y, anchor="center")
        elif keyboard.is_pressed("a") and keyboard.is_pressed("s") and not keyboard.is_pressed("w") and not keyboard.is_pressed("d") and x > 0.0025 and y < 0.995:
            x = x - 0.0015 * 0.7
            y = y + 0.002 * 0.7
            panel.place(relx=x, rely=y, anchor="center")
    except AttributeError:
        pass

    root.update()