import tkinter as tk
import tkinter.font as font

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

window = tk.Tk()
window.configure(bg="black")
window.geometry("100x400+0+0")
window.resizable(0, 0)  # makes the window resizable by x and y number of pixels, in this case, 0

myFont = font.Font(family="Runescape UF", size=15)

combatList = ["Attack", "Strength", "Defense", "Hitpoints", "Ranged", "Magic", "Prayer"]
labelDictionary = {}
entryDictionary = {}

def calculate():

    base = 0.25 * ((int(entryDictionary["Defense"].get())) + int(entryDictionary["Hitpoints"].get()) + math.floor(int(entryDictionary["Prayer"].get())/2))
    melee = 0.325 * (int(entryDictionary["Attack"].get()) + int(entryDictionary["Strength"].get()))
    ranged = 0.325 * (math.floor(3 * int(entryDictionary["Ranged"].get())/2))
    magic = 0.325 * (math.floor( 3 * int(entryDictionary["Magic"].get())/2))
    if melee > ranged and melee > magic:
        final = math.floor(base + melee)
    elif ranged > melee and ranged > magic:
        final = math.floor(base + ranged)
    elif magic > melee and magic > ranged:
        final = math.floor(base + magic)
    labelCombat["text"] = "Combat: " + str(final)
    print(base)
    print(melee)
    print(ranged)
    print(magic)
for i in combatList:
    labelDictionary[i] = tk.Label(window, text=i, bg="black", fg="yellow")
    labelDictionary[i]["font"] = myFont
    labelDictionary[i].pack()
    entryDictionary[i] = tk.Entry(window, width=10, bg="black", fg="yellow")
    entryDictionary[i]["font"] = myFont
    entryDictionary[i].pack()
buttonSubmit = tk.Button(window, text="SUBMIT", bg="black", fg="yellow", command=calculate)
buttonSubmit["font"] = myFont
buttonSubmit.pack()
labelCombat = tk.Label(window, text="Combat: ", bg="black", fg="yellow")
labelCombat["font"] = myFont
labelCombat.pack()



window.mainloop()
