import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text To Speech")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="#872657")

engine = pyttsx3.init()


# ---------------- SPEAK FUNCTION ----------------
def speaknow():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    if text == "":
        return

    # Speed settings
    if speed == "Fast":
        engine.setProperty('rate', 250)
    elif speed == "Normal":
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    # Voice settings
    if gender == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()


# ---------------- DOWNLOAD FUNCTION ----------------
def download():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    if text == "":
        return

    # Speed settings
    if speed == "Fast":
        engine.setProperty('rate', 250)
    elif speed == "Normal":
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    # Choose location to save file
    path = filedialog.askdirectory()
    if path == "":
        return

    os.chdir(path)

    # Voice settings
    if gender == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.save_to_file(text, 'text.mp3')
    engine.runAndWait()


# ---------------- UI DESIGN ----------------

# Top frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

# NOTE: Change image paths based on your folder
Logo = PhotoImage(file="IMAGES/mic2.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=70, y=30)

# Text area
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# Labels
Label(root, text="VOICE", font="arial 15 bold", bg="#000000", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#000000", fg="white").place(x=760, y=160)

# Combobox – Gender
gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

# Combobox – Speed
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

# Buttons
imageicon = PhotoImage(file="IMAGES/sp1.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file="IMAGES/d1.jpg")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=130, bg="#000000",
              font="arial 14 bold", fg="white", command=download)
save.place(x=730, y=280)

root.mainloop()
