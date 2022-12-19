from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        # self.window.minsize(width=300, height=600)
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="soru",
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        next_questin = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=next_questin)
