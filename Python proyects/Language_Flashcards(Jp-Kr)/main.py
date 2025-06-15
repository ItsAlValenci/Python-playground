from tkinter import *
import pandas as pd
import random

jp_lang_pack = ("data/Essential_Japanese.csv")
kr_lang_pack = ("data/Essential_Korean.csv")

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial",40,"italic")
FONT_WORD = ("Arial",60,"bold")

icone_card = ("images/card_front.png")
icone_card_back = ("./images/card_back.png")
icone_check = ("images/right.png")
icone_cross = ("./images/wrong.png")

current_word = {}
to_learn = {}


# ---------------------------- GETTING LANGUAGE ------------------------------- # 
try:
    language_data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    language_data = pd.read_csv(kr_lang_pack)
    to_learn = language_data.to_dict(orient= "records")

else:
    to_learn = language_data.to_dict(orient= "records")

# ---------------------------- GETTINNG WORDS ------------------------------- # 

def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    word_to_display = current_word["Korean"]
    canvas.itemconfig(language_label,text= "Korean", fill= "black")
    canvas.itemconfig(word_label,text= word_to_display,fill= "black")
    canvas.itemconfig(canvas_image, image= front_card)
    flip_timer = window.after(5000, flip_card)



# ---------------------------- T ------------------------------- # 
def flip_card():
    canvas.itemconfig(language_label,text= "English",fill= "white")
    canvas.itemconfig(word_label,text= current_word["English"], fill= "white")
    canvas.itemconfig(canvas_image, image= back_card)

# ---------------------------- BUTTOS ACTIONS ------------------------------- # 

def i_know_it():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_word()



def i_dont_know_it():
    next_word()


# ---------------------------- UI ------------------------------- # 

window = Tk()
window.title("Language Flashcards for Jp & Kr")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

#timer for the car reveal
flip_timer = window.after(5000, flip_card)

#Loading Card Images
front_card = PhotoImage(file= icone_card)
back_card = PhotoImage(file= icone_card_back)

#Creating Canvas (CARD)
canvas = Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness=0)

canvas_image = canvas.create_image(400,263, image=front_card )
language_label = canvas.create_text(400,150,text= "Language", font=FONT_LANGUAGE, fill= "black")
word_label = canvas.create_text(400,263,text= "word", font=FONT_WORD, fill= "black")
canvas.grid(column=0,row=0, columnspan=2)

#Loading Button Images
yay_button = PhotoImage(file= icone_check)
ney_button = PhotoImage(file= icone_cross)

#creating Buttons
known_button = Button(image= yay_button, highlightthickness=0, command=i_know_it)
known_button.grid(column=1,row=1)

unknown_button = Button(image= ney_button, highlightthickness=0, command= i_dont_know_it)
unknown_button.grid(column=0,row=1)

active_word = next_word()



window.mainloop()
