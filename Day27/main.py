from tkinter import *

window = Tk()
window.title("my first GUI program")
window.minsize(width=400, height=400)

entry_string = "I am a label"
my_label = Label(text=entry_string , font=("Arial", 24))
my_label.pack()  # pack() modülü ortaya yazılmasını sağlıyor


# Button

def clicked_button():
    entry_string = input.get()
    my_label.config(text=entry_string)


button = Button(text="Click Me.", command=clicked_button)
button.pack()

# Entry

input = Entry()
input.pack()









window.mainloop()
