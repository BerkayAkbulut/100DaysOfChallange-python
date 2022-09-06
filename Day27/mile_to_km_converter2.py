from tkinter import *


def calculate():
    mil = int(enrty.get())
    mil *= 1.609344
    result.config(text=mil)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

enrty = Entry(width=10)
enrty.grid(column=1, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

result = Label(text=0)
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
