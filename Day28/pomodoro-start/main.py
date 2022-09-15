from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 7
LONG_BREAK_MIN = 5
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def get_started():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    sec_count = count % 60
    min_count = int(count / 60)

    if sec_count < 10:
        sec_count = '0' + str(sec_count)

    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        get_started()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)

start = Button(text="Start", highlightthickness=0, command=get_started)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(column=1, row=0)

window.mainloop()
