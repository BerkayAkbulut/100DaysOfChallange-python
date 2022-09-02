import tkinter

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=400, height=400)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()  # pack() modülü ortaya yazılmasını sağlıyor

window.mainloop()
