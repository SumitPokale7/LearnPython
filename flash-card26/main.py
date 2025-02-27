from tkinter import *
from tkinter import messagebox
import pandas
import random



# ---------------------------- CONSTANTS -------------------------------- #
try:
    DATA = pandas.read_csv(r"E:\\College\\Python\\flash-card26\\data\\words_to_learn.csv")
except FileNotFoundError:
    DATA = pandas.read_csv(r"E:\\College\\Python\\flash-card26\\data\\french_words.csv")

WORDS_LIST = DATA.to_dict(orient="records")
FONT_NAME = "Arial"
BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}


# ---------------------------- KNOWN CARD/WORD --------------------------- #
def is_known():
    global WORDS_LIST

    try:
        WORDS_LIST.remove(CURRENT_CARD)
    except ValueError:
        pass

    new_word_list = pandas.DataFrame(WORDS_LIST)
    new_word_list.to_csv("data/words_to_learn.csv", index=False)

    next_card()



# ---------------------------- NEXT CARD -------------------------------- #
def next_card():
    global CURRENT_CARD, FLIP_TIMER
    window.after_cancel(FLIP_TIMER)
    CURRENT_CARD = random.choice(WORDS_LIST)

    canvas.itemconfig(cards_title, text='French', fill="black")
    canvas.itemconfig(cards_word, text=CURRENT_CARD['French'], fill="black")
    canvas.itemconfig(canvas_background, image=card_front_img)

    FLIP_TIMER = window.after(3000, func=flip_card)



# ---------------------------- CHANGE CARDS --------------------------- #
def flip_card():
    canvas.itemconfig(cards_title, text="English", fill="white")
    canvas.itemconfig(cards_word, text=CURRENT_CARD['English'], fill="white")
    canvas.itemconfig(canvas_background, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

FLIP_TIMER = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=r"E:\\College\\Python\\flash-card26\\images\\card_front.png")
card_back_img = PhotoImage(file=r"E:\\College\\Python\\flash-card26\\images\\card_back.png")


canvas_background = canvas.create_image(400, 263,image=card_front_img)
cards_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
cards_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_img = PhotoImage(file=r"E:\\College\\Python\\flash-card26\\images\\wrong.png")
unkown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unkown_button.grid(row=1, column=0)


check_img = PhotoImage(file=r"E:\\College\\Python\\flash-card26\\images\\right.png")
know_button = Button(image=check_img, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)




next_card()


window.mainloop()
