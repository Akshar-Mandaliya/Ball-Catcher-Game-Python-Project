## LIST OF MODULE(ITERTOLLS , RANDON AND TKINTER MODULE USING GAME)
from itertools import cycle
from random import randrange
from tkinter import Canvas,Tk, messagebox, font
## SCREEN SIZE OF BALL CATCHER GAME
canvas_width = 1000
canvas_height = 600
root = Tk()
##GAME TITLE
root.title("MANDALIYA AKSHAR , MANDALIYA OM , PIPLIYA AKSHAY , NANDOLA AAYUSH")
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
## CANVAS BOTTOM SIZE 
c.create_rectangle(-5, canvas_height-100, canvas_width+10, canvas_height+20, fill="sea green", width=0)
c.pack()
## BALL MOVE TO TOP COLOR IN BALL
color_cycle = cycle(["light PINK", "light green", "light pink", "light yellow", "light cyan"])
## EGG WIDTH,HEIGHT,SCORE AND INTERVALUE
egg_width = 80
egg_height = 80
egg_score = 5
egg_speed = 100
egg_interval = 4000
## BALL SPEED
difficulty =1
## CATCHER COLOR
catcher_color = "purple"
## CATCHER WIDTH IN BOTTOM
catcher_width = 200
## CATCHER HEIGHT IN SCREEN
catcher_height = 200
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height
catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
game_font = font.nametofont("TkFixedFont")
## FONT SIZE IN GAME (SCORE AND LIFELINE)
game_font.config(size=18)
## SCORE FUNCTION DISPLAY
score = 0
score_text = c.create_text(20, 20, anchor="nw", font=game_font, fill="darkorange", text="Score: "+ str(score))
## LIFELINE FUNCTION DISPLAY
lifeline_remaining = 3
lifeline_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkgreen", text="Lifeline: "+ str(lifeline_remaining))
BALLS = []
##craete a egg on the screen
def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    BALLS.append(new_egg)
    root.after(egg_interval, create_egg)
    ##move the balls 
def move_BALLS():
    for egg in BALLS:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg, 0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_BALLS)
## GAME FINISH OUT THE PRINT ON SCREEN
def egg_dropped(egg):
    BALLS.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lifeline_remaining == 0:
        messagebox.showinfo("GAME FINISH!", "FINAL SCORE: "+ str(score))
        root.destroy()
## LIFELINE SHOW ON SCREEN FUNCTION 
def lose_a_life():
    global lifeline_remaining
    lifeline_remaining -= 1
    c.itemconfigure(lifeline_text, text="Lifeline: "+ str(lifeline_remaining))
## CANVAS CATCH ON SCREEN FUNCTION 
def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in BALLS:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            BALLS.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(200, check_catch)
    
## INCREASE THE SCORE OF FUNCTION 
def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    c.itemconfigure(score_text, text="Score: "+ str(score))
## MOVE LEFT SIDE IN CANVAS
def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)
## MOVE THE RIGHT SIDE IN CANVAS
def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)


## CATCHER LEFT FUNCTION
c.bind("<Left>", move_left)
## CATCHER RIGHT FUNCTION 
c.bind("<Right>", move_right)

c.focus_set()
root.after(1000, create_egg)
root.after(1000, move_BALLS)
root.after(1000, check_catch)
root.mainloop()



