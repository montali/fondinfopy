 #!/usr/bin/env python3
'''
@author  Riccardo Fava(287516), Simone Montali(288144)
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''


import game2d

from bounce import *
from constants import *
from dk_elements import map_elements



def setup():
    global arena, sprites , loser, winner, Barrel, Jumper , background
    difficulty=0
    while(difficulty<1):
        difficulty= int(input("Set difficulty from 1 (easy) to 5 (tomamic)"))
    arena = DKArena(ARENA_WIDTH, ARENA_HEIGHT, difficulty)
    game2d.canvas_init(arena.size())
    sprites = game2d.image_load("dk_sprites.png")
    background = game2d.image_load("dk_background.png")
    winner  =   game2d.image_load("winner.png")
    loser = game2d.image_load("loser.png")
    game2d.handle_keyboard(keydown, keyup)
    print_arena(arena)
    for t, x, y, w, h in map_elements:
        if t == "Platform":
            Platform( int(x), int(y), int(w), int(h))
        elif t == "Ladder":
            Ladder(int(x), int(y), int (w), int(h))
        elif t == "interruptedLadder":
            interruptedLadder(int(x), int(y),int(w), int(h))
    game2d.set_interval(dropper, DROPPER_INTERVAL//difficulty)  # 30 secs is the maximum amount, 6 the minimum
    game2d.set_interval(positionUpdater,POSITION_UPDATE_INTERVAL) #this things updates dks and peaches position every 0.5 secs
    game2d.set_interval(update, UPDATE_INTERVAL) #This one updates the arena

def update():
    if not (arena.won() or arena.lost()):
        arena.move_all()
        game2d.image_blit(background,(0,0))
        for a in arena.actors():
            x, y, w, h = a.rect()
            xs, ys = a.symbol()
            game2d.image_blit(sprites, (x, y), area=(xs, ys, w, h))
    elif (arena.won()):
        game2d.image_blit(winner,(0,0))
    elif (arena.lost()):
        game2d.image_blit(loser,(0,0))

def dropper ():
    arena.dropBarrel()
def positionUpdater ():
    arena.updateActorsPosition()
def keydown(code):
    if (code=="ArrowLeft"):
        arena.marioLeft()
    elif (code=="ArrowRight"):
        arena.marioRight()
    if(code=="Space"):
        arena.marioJump()
    if(code=="ArrowUp"):
        arena.marioUp()

def keyup(code):
    if (code=="ArrowLeft" or code == "ArrowRight" or code == "ArrowUp"):
        arena.marioStay()

setup()
