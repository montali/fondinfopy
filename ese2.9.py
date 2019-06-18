#------------------------------
# Name: Esercizio 2.9
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

import game2d

WIDTH=1200
HEIGHT=800
SIDE=100

def keydown (code: str):
    global dx
    global dy
    if (code=="ArrowLeft"):
        dx=-5
    if (code=="ArrowRight"):
        dx=5
    if (code=="ArrowUp"):
        dy=-5
    if(code=="ArrowDown"):
        dy=5

def keyup (code: str):
    global dx
    global dy
    if (code=="ArrowLeft" or code == "ArrowRight"):
        dx=0
    if (code=="ArrowUp" or code=="ArrowDown"):
        dy=0

def update():
    global dx
    global dy
    global x
    global y
    game2d.canvas_fill((255, 255, 255))
    game2d.draw_rect((0,0,255),(x,y,SIDE,SIDE))
    if ((x+dx)<0):
        x=0
    elif((x+dx)>(WIDTH-SIDE)):
        x=(WIDTH-SIDE)
    else:
        x+=dx
    if ((y+dy)<0):
        y=0
    elif ((y+dy)>(HEIGHT-SIDE)):
        y=(HEIGHT-SIDE)
    else:
        y+=dy

game2d.canvas_init((WIDTH, HEIGHT))
dx = 0
dy = 0
x = 50
y = 50
game2d.handle_keyboard(keydown,keyup)
game2d.set_interval(update, 1000 // 30)
