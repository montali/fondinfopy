#------------------------------
# Name: Esercizio 3.1ese
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

import game2d
import random
ARENA_W=500
ARENA_H=500

class Ball:

    def __init__(self, x, y)    :
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5
        self._w = 20
        self._h = 20

    def move(self):
        self._x += self._dx
        if (self._x>(ARENA_W-self._w)):
            self._x=self._w

    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def draw(self):
        game2d.draw_circle((0,0,255),(self._x,self._y),self._w)

game2d.canvas_init((ARENA_W,ARENA_H))
b2 = Ball(80, 40)
print('Ball 2 @', b2.rect())

while input() != 'x':
    game2d.canvas_fill((255, 255, 255))
    b2.move()
    b2.draw()
    print('Ball 2 @', b2.rect())
