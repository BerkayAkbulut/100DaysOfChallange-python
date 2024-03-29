from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    input_password.delete(0, 'end')

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pasword_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + pasword_numbers

    random.shuffle(password_list)

    passwordd = "".join(password_list)
    pyperclip.copy(passwordd)
    input_password.insert(0, passwordd)
    # print(f"Your password is: {passwordd}")


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


label_web_site = Label(text="Website : ")
label_web_site.grid(row=1, column=0)

label_email = Label(text="Email / Username : ")
label_email.grid(row=2, column=0)

label_password = Label(text="Password : ")
label_password.grid(row=3, column=0)

# INPUTS
# Entries
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

input_email = Entry(width=35)
input_email.grid(row=2, column=1, pady=5, columnspan=2)
input_email.insert(0, "email@example.com")

input_password = Entry(width=21)
input_password.grid(row=3, column=1)

# BUTTONS
# Buttons
button_gen_pass = Button(text="Generate Password", command=generate_password)
button_gen_pass.grid(row=3, column=2)

add_button = Button(text="Add Password", width=36, command=save)
add_button.grid(row=4, column=1, pady=5, columnspan=2)

window.mainloop()
