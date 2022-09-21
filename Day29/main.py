from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if input_password.get() == "" or input_website.get() == "":
        messagebox.showwarning(title="Oops!", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=input_website.get(),
                                       message=f"These are the details entered: \nEmail: {input_email.get()}"
                                               f" \nPassword:{input_password.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{input_website.get()} | {input_email.get()} | {input_password.get()} \n")

            input_website.delete(0, 'end')
            # input_email.delete(0, 'end')
            input_password.delete(0, 'end')
            print("saved")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

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
input_website.focus()
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "akbulutberkay@yandex.com")
input_password = Entry(width=17)
input_password.grid(column=1, row=3)

# BUTTONS
button_gen_pass = Button(text="Generate Password")
button_gen_pass.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4)

window.mainloop()
