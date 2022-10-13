from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
NUM = 0

data = pd.read_csv("data/french_words.csv")
data = data.to_dict()


def create_card():
    i = random.randint(0, 100)
    global NUM
    NUM = i
    canvas.itemconfig(title, text="French")
    try:
        canvas.itemconfig(word, text=f"{data['French'][i]}")
    except KeyError:
        i = random.randint(0, 100)
    finally:
        canvas.itemconfig(word, text=f"{data['French'][i]}")
    windows.after(3000, flip_card)


def flip_card():
    global NUM
    i = NUM
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=f"{data['English'][i]}")


def right():
    global NUM
    i = NUM
    data['French'].pop(i)
    data['English'].pop(i)
    create_card()


def wrong():
    create_card()


windows = Tk()
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

en = PhotoImage(file="images/card_back.png")
fr = PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
create_image = canvas.create_image(400, 263, image=fr)
title = canvas.create_text(400, 150, text="", font=("Aerial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Aerial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_b = Button(image=right_image, highlightthickness=0, command=right)
right_b.grid(row=1, column=1)

wrong_b = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_b.grid(row=1, column=0)

create_card()
windows.mainloop()
