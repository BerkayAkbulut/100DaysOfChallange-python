import random
from tkinter import *
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
WORD = "word"

current_card = {}

# ------------TIMING--------------------------

def newWord():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(df_list)

    canvas.itemconfig(card_backgroud, image=flashcard)
    canvas.itemconfig(lang_of_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_backgroud, image=back_flashcard)
    canvas.itemconfig(lang_of_text, text="Türkçe", fill="white")
    canvas.itemconfig(word_text, text=current_card["Turkish"], fill="white")

def is_know():
    df_list.remove(current_card)
    print(len(df_list))

    data=pd.DataFrame(df_list)
    data.to_csv('data/known_words.csv', index=False)

    newWord()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)

flashcard = PhotoImage(file="images/card_front.png")
back_flashcard = PhotoImage(file="images/card_back.png")
card_backgroud = canvas.create_image(400, 263, image=flashcard)
canvas.grid(column=0, row=0, columnspan=2)

# LABELS
lang_of_text = canvas.create_text(400, 150, text="Title", fill="black", font=('Ariel 40 italic'))
word_text = canvas.create_text(400, 263, text=WORD, fill="black", font=('Ariel 60 bold'))

# BUTTONS
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=newWord)
wrong_button.grid(column=0, row=1, padx=50, pady=20)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(column=1, row=1, padx=50, pady=20)

# Read data
try:
    df = pd.read_csv("data/known_words.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/english_words copy.csv")
    df_list = original_df.to_dict(orient="records")
else:
    df_list = df.to_dict(orient="records")

newWord()
# window.after(3000,newWord_Tr(current_card))
# newWord_Tr(current_card)


window.mainloop()
