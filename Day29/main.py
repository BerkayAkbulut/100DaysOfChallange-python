from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200)

lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# LABELS
label_web_site = Label(text='Website :')
label_web_site.grid(column=0, row=1)
label_email = Label(text="E-mail/Username :")
label_email.grid(column=0, row=2)
label_password = Label(text="Password :")
label_password.grid(column=0, row=3)

# INPUTS
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_password = Entry(width=17)
input_password.grid(column=1, row=3)

# BUTTONS
button_gen_pass = Button(text="Generate Password")
button_gen_pass.grid(column=2, row=3)
button_add = Button(text="Add", width=36)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
