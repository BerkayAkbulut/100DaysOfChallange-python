from tkinter import *


def clicked_button():
    entry_string = input.get()
    my_label.config(text=entry_string)


window = Tk()
window.title("my first GUI program")
window.minsize(width=400, height=400)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()  # pack() modülü ortaya yazılmasını sağlıyor

# Button
button = Button(text="Click Me.", command=clicked_button)
button.pack()

# Entry
input = Entry()
input.pack()

window.mainloop()
