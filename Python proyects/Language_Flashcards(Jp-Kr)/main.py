from tkinter import *
import pandas as pd
import random

jp_lang_pack = ("data/Essential_Japanese.csv")
kr_lang_pack = ("data/Essential_Korean.csv")

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial",40,"italic")
FONT_WORD = ("Arial",60,"bold")

LANG_CONFIG = {
    "KR": {
        "name": "Korean",
        "original_file": "data/Essential_Korean.csv",
        "still_learning": "data/words_to_learn_kr.csv"
    },
    "JP": {
        "name": "Japanese",
        "original_file": "data/Essential_Japanese.csv",
        "still_learning": "data/words_to_learn_jp.csv"
    }
}

icone_card = ("images/card_front.png")
icone_card_back = ("./images/card_back.png")
icone_check = ("images/right.png")
icone_cross = ("./images/wrong.png")

current_word = {}
to_learn = {}

flip_timer = None

active_language = "JP"

# ---------------------------- GETTING LANGUAGE ------------------------------- # 

# if active_language == "KR":
#     try:
#         language_data = pd.read_csv("data/words_to_learn_kr.csv")

#     except FileNotFoundError:
#         language_data = pd.read_csv(kr_lang_pack)
#         to_learn = language_data.to_dict(orient= "records")

#     else:
#         to_learn = language_data.to_dict(orient= "records")

# elif active_language == "JP":
#     try:
#         language_data = pd.read_csv("data/words_to_learn_jp.csv")

#     except FileNotFoundError:
#         language_data = pd.read_csv(jp_lang_pack)
#         to_learn = language_data.to_dict(orient= "records")

#     else:
#         to_learn = language_data.to_dict(orient= "records")

def load_language_data(language_code):
    config = LANG_CONFIG[language_code]
    try:
        data = pd.read_csv(config["still_learning"])
    except FileNotFoundError:
        data = pd.read_csv(config["original_file"])
    return data.to_dict(orient="records")

to_learn = load_language_data(active_language)

# ---------------------------- GETTINNG WORDS ------------------------------- # 

def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    lang_on_screen = LANG_CONFIG[active_language]["name"]
    
    canvas.itemconfig(language_label, text=lang_on_screen, fill="black")
    canvas.itemconfig(word_label, text=current_word[lang_on_screen], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = window.after(5000, flip_card)

# def flip_card():
#     canvas.itemconfig(language_label,text= "English",fill= "white")
#     canvas.itemconfig(word_label,text= current_word["English"], fill= "white")
#     canvas.itemconfig(canvas_image, image= back_card)

def flip_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_word["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_card)


# ---------------------------- BUTTOS ACTIONS ------------------------------- # 

# def i_know_it():
#     to_learn.remove(current_word)
#     data = pd.DataFrame(to_learn)
#     if active_language == "KR":
#         data.to_csv("data/words_to_learn_kr.csv", index=False)
#     elif active_language == "JP":
#         data.to_csv("data/words_to_learn_jp.csv", index=False)

#     next_word()

def i_know_it():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv(LANG_CONFIG[active_language]["still_learning"], index=False)
    
    next_word()



def i_dont_know_it():
    next_word()

# ---------------------------- INTERACTIONS ------------------------------- # 
def show_language_selection():
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(language_label, text="", fill="black")
    canvas.itemconfig(word_label, text="", fill="black")

    # Load flag images
    global flag_jp_img, flag_kr_img, flag_jp_btn, flag_kr_btn
    flag_jp_img = PhotoImage(file="images/Japan_flag_icon.png")
    flag_kr_img = PhotoImage(file="images/Korean_flag_icon.png")

    # Create buttons for flags
    flag_jp_btn = Button(image=flag_jp_img, highlightthickness=0,borderwidth=0, command=lambda: start_game("JP"))
    flag_kr_btn = Button(image=flag_kr_img, highlightthickness=0,borderwidth=0, command=lambda: start_game("KR"), foreground= "white")

    # Position the flag buttons on the canvas
    canvas.itemconfig(language_label,text= "Choose a Language", font=FONT_LANGUAGE, fill= "black")
    canvas.coords(language_label, 400, 100) 
    canvas.create_window(210, 300, window=flag_jp_btn)
    canvas.create_window(590, 300, window=flag_kr_btn)

def start_game(lang_code):
    global active_language, to_learn
    active_language = lang_code
    to_learn = load_language_data(active_language)

    # Remove flag buttons
    flag_jp_btn.destroy()
    flag_kr_btn.destroy()


    # Displaying Buttons
    known_button.grid()
    unknown_button.grid()

    next_word()


# ---------------------------- UI ------------------------------- # 



window = Tk()
window.title("Language Flashcards for Jp & Kr")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(0, lambda: None)

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
known_button = Button(image= yay_button, highlightthickness=0,borderwidth=0, command=i_know_it)
known_button.grid(column=1,row=1)
known_button.grid_remove()

unknown_button = Button(image= ney_button, highlightthickness=0,borderwidth=0, command= i_dont_know_it)
unknown_button.grid(column=0,row=1)
unknown_button.grid_remove()


show_language_selection()


window.mainloop()
