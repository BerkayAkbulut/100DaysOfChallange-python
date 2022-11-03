from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)

flashcard = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flashcard)
canvas.grid(column=0, row=0, columnspan=2)

# LABELS
canvas.create_text(400, 150, text="Title", fill="black", font=('Ariel 40 italic'))
canvas.create_text(400, 263, text="word", fill="black", font=('Ariel 60 bold'))

# BUTTONS
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1, padx=50, pady=20)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1, padx=50, pady=20)

window.mainloop()
