import math
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

# ---------------------------- GLOBALS ------------------------------- #
timer = NONE  # NONE is a Tkinter constant
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps < 8:
        reps += 1

        if reps == 8:
            timer_label.config(text="Break", fg=RED)
            # count_down(LONG_BREAK_MIN * 60)
            count_down(4)  # Testing
        elif reps % 2 == 0:
            timer_label.config(text="Break", fg=PINK)
            # count_down(SHORT_BREAK_MIN * 60)
            count_down(3)  # Testing
        else:
            timer_label.config(text="Work", fg=GREEN)
            # count_down(WORK_MIN * 60)
            count_down(5)  # Testing


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"

    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    time_remaining = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time_remaining)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # reps is a global variable.
        # Add a check mark to the label after a work session is completed.
        if reps % 2 != 0:
            checks_text = check_marks_label.cget("text")
            checks_text += "✔"
            check_marks_label.config(text=checks_text)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image, anchor="center")
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "normal"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", width=5, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", width=5, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
check_marks_label.grid(row=3, column=1)

window.mainloop()
