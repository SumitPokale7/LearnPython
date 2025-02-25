from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 1
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", foreground=RED, bg=YELLOW, font=(FONT_NAME, 50))
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Short Break", foreground=PINK, bg=YELLOW, font=(FONT_NAME, 50))
    else:
        countdown(work_sec)
        title_label.config(text="Work", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 50))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            marks += "✓"
        checkmark.config(text=marks, foreground=PINK, bg=YELLOW, font=(FONT_NAME, 50))



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, borderwidth=0, relief="flat", bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", highlightthickness=0, borderwidth=0, relief="flat", bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)


checkmark = Label(bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 35))
checkmark.grid(column=1, row=3)


window.mainloop()
