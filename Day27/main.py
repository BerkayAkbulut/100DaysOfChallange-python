from tkinter import *


def clicked_button():
    entry_string = input.get()
    my_label.config(text=entry_string)


window = Tk()
window.title("my first GUI program")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack(side='right')  # pack() modülü ortaya yazılmasını sağlıyor
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20,pady=20) # elementin yanına boşluk bırakmamızı sağlıyor

# Button
button = Button(text="Click Me.", command=clicked_button)
# button.pack(side='right')
button.grid(column=1, row=1)

# Button2
button2 = Button(text="Click Me2.", command=clicked_button)
# button.pack(side='right')
button2.grid(column=2, row=0)

# Entry
input = Entry()
# input.pack(side='right')
input.grid(column=3, row=2)
window.mainloop()
