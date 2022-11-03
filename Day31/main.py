from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR)
canvas.pack_propagate(0)

flashcard = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flashcard)
canvas.grid(column=1, row=0, columnspan=2)

# LABELS
canvas.create_text(400, 150, text="Title", fill="black", font=('Ariel 40 italic'))
canvas.create_text(400, 263, text="Title2", fill="black", font=('Ariel 60 bold'))


window.mainloop()
