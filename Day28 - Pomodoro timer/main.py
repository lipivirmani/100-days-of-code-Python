from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button["state"]= "active"
    # stops the timer
    window.after_cancel(timer)
    # reseting and removing check marks
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # if start button pressed again and again it gives bugs to solve it
    start_button["state"] = "disabled"
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="BREAK", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        time_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60  # Use integer division for clarity
    count_sec = f"{count % 60:02}"  # Format seconds with leading zero
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        bring_window_to_top()
        start_timer()
        completed_sess = reps // 2  # Use integer division
        check_marks.config(text="✔" * completed_sess)


def bring_window_to_top():
    """Ensures the window is brought to the front."""
    window.lift()
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)
    window.focus_force()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize()
window.title("Pomodoro Project")
window.config(pady=100, padx=100, bg=YELLOW)

# adding image to program #
img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
canvas.create_image((100, 115), image=img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 44))
canvas.grid(column=1, row=1)

time_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
time_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=4)

window.mainloop()
