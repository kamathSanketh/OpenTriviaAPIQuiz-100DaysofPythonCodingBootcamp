from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def make_white(self):
        self.canvas.configure(bg="white")
        self.get_next_question()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        score = self.quiz.return_score()
        self.score_label["text"] = "Score :" + str(score)
        self.canvas.itemconfig(self.question_text, text=q_text)
    def false_clicked(self):
        feedback = self.quiz.check_answer("false")
        if feedback == True:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(500, func=self.make_white)
    def true_clicked(self):
        feedback = self.quiz.check_answer("true")
        if feedback == True:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(500, func=self.make_white)
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()
