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
LONG_BREAK_MIN = 20

reps = 0
marks= ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    general_title.config(text="Timer")
    canvas.itemconfig(timer_text, text= "00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0 :
        general_title.config(text= "Break", fg= RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        general_title.config(text= "Break", fg= PINK)
        count_down(short_break_sec)
    else :
        general_title.config(text= "Work Time", fg= GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    else:
        count_sec = f"{int(count_sec)}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000,count_down, count - 1 )
    else:
        start_timer()
        
        if reps % 2 == 0:
            global marks
            marks += "✔"
        check_marks.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro") 
window.config(padx=100, pady= 50, bg=YELLOW)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
my_icone = PhotoImage(file= "tomato.png")
canvas.create_image(100,112, image=my_icone )
timer_text= canvas.create_text(100,130, text= "00:00", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=2,column=2)

#Label
general_title = Label()
general_title.config(text="Timer", bg= YELLOW ,fg=GREEN, font= (FONT_NAME,45))
general_title.grid(row= 1,column=2)

check_marks = Label(fg=GREEN,bg= YELLOW,)
check_marks.grid(row=4,column=2)

#buttons
start_button = Button()
start_button.config(text= "START", bg= YELLOW, highlightthickness=0,bd=0, command=start_timer)
start_button.grid(row=3,column=1)


reset_button = Button()
reset_button.config(text= "RESET", bg= YELLOW, highlightthickness=0,bd=0,command=reset_timer)
reset_button.grid(row=3,column=3)





 
window.mainloop()