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
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps == 8:
        timer.config(text="Break", fg=RED)
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
    if reps % 2 != 0:
        timer.config(text="Work", fg=GREEN)
        work_sec = WORK_MIN * 60
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
check_mark = "✔"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(102, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label

timer = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)
timer.grid(column=1, row=0)

# start button

start = Button(text="start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

# reset button

reset = Button(text="reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

# check_mark label

check = Label(text="", bg=YELLOW, font=(FONT_NAME, 14, "bold"), fg=GREEN)
check.grid(column=1, row=3)

window.mainloop()
