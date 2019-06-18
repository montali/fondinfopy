#------------------------------
# Name: Esercizio 3.9
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

import game2d
import random
ARENA_W=500
ARENA_H=500

def keydown(code: str):
    global balls
    print(code)
    if (code=="ArrowLeft"):
        balls[0].go_left()
    elif (code=="ArrowRight"):
        balls[0].go_right()
    if(code=="Space"):
        balls[0].jump()


def keyup(code: str):
    global balls
    if (code=="ArrowLeft" or code == "ArrowRight"):
        balls[0].stay()






class Ball:

    def __init__(self, x, y, weight)    :
        self._x = x
        self._y = y
        self._weight=weight
        self._dx = 0
        self._dy = 0 #Simuliamo un peso pallina da 10 a 40
        self._w = 20
        self._h = 20
        self._g = 0.4
        self._color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def move(self):
        self._x += self._dx
        if ((self._x)>(ARENA_W+self._w)):
            self._x=self._w
        if((self._w+self._x)<0):
            self._x=(ARENA_W+self._w)
        self._dy+=self._g
        self._y += self._dy
        if (self._y>=(ARENA_H-self._h)):
            self._y=(ARENA_H-self._h)

    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def update (self):
        self.move()
        self.draw()
        print(self._dx)

    def draw(self):
        game2d.draw_circle(self._color,(self._x,self._y),self._w)

    def go_left (self):
        print("left"  )
        self._dx=-5

    def go_right (self):
        self._dx=5

    def stay (self):
        self._dx=0

    def jump (self):
        if(self._y==(ARENA_H-self._h)):
            self._dy=-15

def updateall ():
    game2d.canvas_fill((255, 255, 255))
    for b in balls:
        b.update()

game2d.canvas_init((ARENA_W,ARENA_H))
balls=[]
balls.append(Ball(random.randint(0, ARENA_W),random.randint(0,ARENA_H),random.randint(10,40)))

game2d.handle_keyboard(keydown,keyup)
game2d.set_interval(updateall,1000//30)
