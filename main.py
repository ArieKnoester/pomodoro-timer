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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1 * 60)


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
        window.after(1000, count_down, count - 1)


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

reset_button = Button(text="Reset", width=5)
reset_button.grid(row=2, column=2)

checks_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
checks_label.grid(row=3, column=1)

window.mainloop()
