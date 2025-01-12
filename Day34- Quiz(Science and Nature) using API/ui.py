from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#7509e8"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz= quiz_brain
        self.window = Tk()
        self.window.title("QUIZ Game")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_label= Label(text="Score : 0 ", fg ="white", bg=THEME_COLOR, font=("Arial", 18))
        self.score_label.grid(row=0 ,column=1)

        self.canvas= Canvas(width=400, height=300,bg= "white")
        self.question_text = self.canvas.create_text(
            200,
            150,
            width= 350 ,
            text="Some Question text",
            fill= THEME_COLOR,
            font= ("Arial",20, "italic"))

        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button= Button(image=true_image, highlightthickness=0, command=self.true_pres)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button= Button(image=false_image, highlightthickness=0, command= self.false_pres)
        self.false_button.grid(row=2, column=1)

        self.get_next_window()

        self.window.mainloop()

    def get_next_window(self):

        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pres(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pres(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="light green")
        else :
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_window)
