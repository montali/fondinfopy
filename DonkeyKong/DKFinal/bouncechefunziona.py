#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random
from actor import *
'''
class Jumper(Actor):

    def __init__(self, arena, x, y):
        self._x = x
        self._y = y
        self._dx = 0
        self._dy = 0
        self._w = 20
        self._h = 20
        self._g = 0.4
        self._max_speed=4
        self._speed=3
        self._arena = arena
        self._onPlatform = False
        self._onLadder = False
        self._alive = True
        self._ladder= None
        arena.add(self)


    def move(self):
        arena_w, arena_h = self._arena.size()
        if self._alive == True:
            self._x += self._dx
            if ((self._x)>(arena_w+self._w)):
                self._x=self._x
            if((self._w+self._x)<0):
                self._x=(arena_w+self._w)
            if self._dy==0:
                self._onPlatform = True
            else:
                self._onPlatform = False
            if not self._onLadder:
                self._dy+=self._g
            self._y += self._dy
            if (self._y>=(arena_h-self._h)):
                self._y=(arena_h-self._h)
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._dx != 0 and self._onLadder:
            self._onLadder = False
            self._dy = 0
        if not (self._onPlatform or self._onLadder):
            self._dy += self._g
            self._dy = min(self._dy, self._max_speed)

        self._onLadder = False

        if self._ladder != None:
            bx, by, bw, bh = self.rect()  # jumper's pos
            wx, wy, ww, wh = self._ladder.rect() # ladder's pos
            if not (wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
                if self._climbing:
                    self._y -= self._dy
                else:
                    self._ladder = None

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w



    def go_left (self):
        self._dx=-5

    def go_right (self):
        self._dx=5

    def stay (self):
        self._dx=0
        self._dy=0

    def go_up (self):
        if self._ladder and (self._climbing or self._landed):
            self._climbing = True
            self._dy = -self._speed

    def go_down (self):
        if self._ladder and (self._climbing or self._landed):
            self._climbing = True
            self._dy = self._speed

    def jump (self):
        arena_w, arena_h = self._arena.size()
        if(self._onPlatform==True):
            self._dy=-3

    def collide(self, other):
        x, y, w, h = other.rect()
        if (isinstance(other, Ladder) and
            wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
            self._ladder = other
        elif isinstance(other, Platform) and not self._onLadder:
            if by + bh < wy + wh:
                self._y = wy - bh
                self._onPlatform = True
        elif isinstance(other, Barrel) and wy <= by + bh // 2 <= wy + wh:
            self._arena.remove(self)


    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._alive == False:
            return 130,106
        else:
            return 93,3
'''

class Jumper(Actor):

    def __init__(self, arena, x, y):
        self._w, self._h = 16, 16
        self._speed = 3
        self._max_speed = 3
        self._gravity = 0.4
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._landed = False
        self._climbing = False
        self._ladder = None
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._dx != 0 and self._climbing:
            self._climbing = False
            self._dy = 0
        if not (self._landed or self._climbing):
            self._dy += self._gravity
            self._dy = min(self._dy, self._max_speed)

        self._landed = False

        if self._ladder != None:
            bx, by, bw, bh = self.rect()  # jumper's pos
            wx, wy, ww, wh = self._ladder.rect() # ladder's pos
            if not (wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
                if self._climbing:
                    self._y -= self._dy
                else:
                    self._ladder = None

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def jump(self):
        if self._landed:
            self._dy = -self._max_speed
            self._landed = False

    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = +self._speed

    def go_up(self):
        if self._ladder and (self._climbing or self._landed):
            self._climbing = True
            self._dy = -self._speed

    def go_down(self):
        if self._ladder and (self._climbing or self._landed):
            self._climbing = True
            self._dy = self._speed

    def stay(self):
        self._dx = 0
        self._dy = 0

    def collide(self, other):
        bx, by, bw, bh = self.rect()  # jumper's pos
        wx, wy, ww, wh = other.rect() # other's pos
        if (isinstance(other, Ladder) and
            wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
            self._ladder = other
        elif isinstance(other, Platform) and not self._climbing:
            if by + bh < wy + wh:
                self._y = wy - bh
                self._landed = True
        elif isinstance(other, Barrel) and wy <= by + bh // 2 <= wy + wh:
            self._arena.remove(self)

    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._climbing:
            return 124, 24
        return 92, 2


class Platform(Actor):
    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        print("blblblb")

    def rect(self):
        return self._x, self._y, self._w, self._h


    def symbol(self):
        return 222,226

class Ladder(Actor):
    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return -1,-1

class Barrel (Jumper):
    def __init__(self, arena, x, y):
        Jumper.__init__(self, arena, x, y)
        self._x = x
        self._y = y
        self._dx = 2.5
        self._dy = 2
        self._w = 12
        self._h = 12
        self._g = 0.4
        self._color = ((0,0,255))
        self._arena = arena
        self._max_speed=4
        self._speed=4
        self._onPlatform = False
        self._onLadder = False
        self._onFire=False
        self._alive=True
        self._ladder=None
        arena.add(self)


    def move(self):
        aw, ah = self._arena.size()
        if self._x + self._w >= aw:
            self.go_left()
        elif self._x <= 0:
            self.go_right()
            if self._y + self._h * 2 > ah:
                self._arena.remove(self)
        Jumper.move(self)
        '''
        self._x += self._dx
        if not (self._onLadder):
            self._dy=0
        if ((self._x)>(arena_w-self._w)):
            self._dx*=-1
        if((self._w+self._x)<0):
            self._dx*=-1
        if self._dy==0:
            self._onPlatform = True
        else:
            self._onPlatform = False
        if not self._onLadder:
            self._dy+=self._g
        self._y += self._dy
        if self._onLadder:
            if (random.randint(0,3)==1):
                self.go_down()
            if (random.randint(0,3)==1) and self._onFire:
                self.go_up()
        if (self._y>=(arena_h-self._h)):
            self._y=(arena_h-self._h)
        if (self._y == (arena_h-self._h)) and (self._x<0):
            if (random.randint(0,3)==1):
                self._onFire=True
            else:
                self._x=-50
                self._dx=0
        print(self._dy,self._g)
        '''

    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if(self._onFire):
            self._h= 25
            self._w=15
            return 125,255
        else:
            return 66,256

def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.rect())


def main():
    global arena
    arena = Arena(320, 240)
  #  Ball(arena, 40, 80)
#    Ball(arena, 80, 40)
#    Ghost(arena, 120, 80)
    Jumper(arena, 50, 100)
    map_elements = [Platform(88, 56, 16, 8),
Platform(104, 56, 16, 8),
Platform(0, 84, 16, 8),
Platform(16, 84, 16, 8),
Platform(32, 84, 16, 8),
Platform(48, 84, 16, 8),
Platform(64, 84, 16, 8),
Platform(80, 84, 16, 8),
Platform(96, 84, 16, 8),
Platform(112, 84, 16, 8),
Platform(128, 84, 16, 8),
Platform(144, 85, 16, 8),
Platform(160, 86, 16, 8),
Platform(176, 87, 16, 8),
Platform(192, 88, 16, 8),
Platform(16, 121, 16, 8),
Platform(32, 120, 16, 8),
Platform(48, 119, 16, 8),
Platform(64, 118, 16, 8),
Platform(80, 117, 16, 8),
Platform(96, 116, 16, 8),
Platform(112, 115, 16, 8),
Platform(128, 114, 16, 8),
Platform(144, 113, 16, 8),
Platform(160, 112, 16, 8),
Platform(176, 111, 16, 8),
Platform(192, 110, 16, 8),
Platform(208, 109, 16, 8),
Platform(0, 142, 16, 8),
Platform(16, 143, 16, 8),
Platform(32, 144, 16, 8),
Platform(48, 145, 16, 8),
Platform(64, 146, 16, 8),
Platform(80, 147, 16, 8),
Platform(96, 148, 16, 8),
Platform(112, 149, 16, 8),
Platform(128, 150, 16, 8),
Platform(144, 151, 16, 8),
Platform(160, 152, 16, 8),
Platform(176, 153, 16, 8),
Platform(192, 154, 16, 8),
Platform(16, 187, 16, 8),
Platform(32, 186, 16, 8),
Platform(48, 185, 16, 8),
Platform(64, 184, 16, 8),
Platform(80, 183, 16, 8),
Platform(96, 182, 16, 8),
Platform(112, 181, 16, 8),
Platform(128, 180, 16, 8),
Platform(144, 179, 16, 8),
Platform(160, 178, 16, 8),
Platform(176, 177, 16, 8),
Platform(192, 176, 16, 8),
Platform(208, 175, 16, 8),
Platform(0, 208, 16, 8),
Platform(16, 209, 16, 8),
Platform(32, 210, 16, 8),
Platform(48, 211, 16, 8),
Platform(64, 212, 16, 8),
Platform(80, 213, 16, 8),
Platform(96, 214, 16, 8),
Platform(112, 215, 16, 8),
Platform(128, 216, 16, 8),
Platform(144, 217, 16, 8),
Platform(160, 218, 16, 8),
Platform(176, 219, 16, 8),
Platform(192, 220, 16, 8),
Platform(0, 248, 16, 8),
Platform(16, 248, 16, 8),
Platform(32, 248, 16, 8),
Platform(48, 248, 16, 8),
Platform(64, 248, 16, 8),
Platform(80, 248, 16, 8),
Platform(96, 248, 16, 8),
Platform(112, 247, 16, 8),
Platform(128, 246, 16, 8),
Platform(144, 245, 16, 8),
Platform(160, 244, 16, 8),
Platform(176, 243, 16, 8),
Platform(192, 242, 16, 8),
Platform(208, 241, 16, 8),
Ladder( 80, 211, 8, 40),
Ladder( 184, 217, 8, 28),
Ladder( 96, 180, 8, 36),
Ladder( 32, 184, 8, 28),
Ladder( 64, 144, 8, 42),
Ladder( 112, 147, 8, 36),
Ladder( 184, 151, 8, 28),
Ladder( 168, 109, 8, 46),
Ladder( 72, 115, 8, 34),
Ladder( 32, 118, 8, 28),
Ladder( 88, 82, 8, 36),
Ladder( 184, 86, 8, 28),
Ladder( 128, 54, 8, 32),
Ladder( 128, 54, 8, 32),
Ladder( 80, 22, 8, 64),
Ladder( 64, 22, 8, 64)]
    print_arena(arena)
    print(random.randint(2,10))
    while input() != 'x':
        arena.move_all()
        print_arena(arena)

if __name__ == '__main__':
    main()
