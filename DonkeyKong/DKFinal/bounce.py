#!/usr/bin/env python3
'''
@author  Riccardo Fava(287516), Simone Montali(288144)
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random
from actor import *
from constants import *

class Jumper(Actor):

    def __init__(self, arena, x, y):
        self._w, self._h = JUMPER_WIDTH, JUMPER_HEIGHT
        self._speed = JUMPER_MAX_SPEED
        self._max_speed = JUMPER_MAX_SPEED
        self._gravity = GRAVITY
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._landed = False
        self._climbing = False
        self._ladder = None
        self._arena = arena
        self._alive=True
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
            self._alive=False

    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._climbing:
            if self._y%2==0:
                return MARIO_CLIMBING1
            else:
                return MARIO_CLIMBING2
        if self._dx<0:
            if self._x%2==0:
                return MARIO_GOINGLEFT1
            else:
                return MARIO_GOINGLEFT2
        elif self._dx>0:
            if self._x%2==0:
                return MARIO_GOINGRIGHT1
            else:
                return MARIO_GOINGRIGHT2
        elif self._dx==0:
            return MARIO_STILL


class Platform(Actor):
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
        return PLATFORM

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
        return EMPTY_SPRITE

class interruptedLadder(Actor):
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
        return EMPTY_SPRITE

class Barrel (Actor):
    def __init__(self, arena, x, y):
        Jumper.__init__(self, arena, x, y)
        self._x = x
        self._y = y
        self._dx = BARREL_DX
        self._dy = BARREL_DY
        self._w = BARREL_WIDTH
        self._h = BARREL_HEIGHT
        self._g = GRAVITY
        self._arena = arena
        self._onPlatform = False
        self._onLadder = False
        self._onFire=False
        self._ladder=None
        self._jumped=False
        arena.add(self)


    def move(self):
        aw, ah = self._arena.size()
        if self._x + self._w >= aw or self._x <= 0:
            self._dx*=-1
            if self._y + self._h * 2 > ah and not self._onFire:
                if(random.randint(0,2)==0):
                    self._arena.remove(self)
                else:
                    self._onFire=True
                    self._x+=20 #moving the barrel to the right
                    self._y-=13
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        # Verifica scale
        if self._ladder != None:
            bx, by, bw, bh = self.rect()  # jumper's pos
            wx, wy, ww, wh = self._ladder.rect() # ladder's pos
            if not self._onFire:
                if (wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
                    if (random.randint(0,3)==1):
                        self._onLadder=True
                    if self._onLadder:
                        self._y += self._dy
                else:
                    self._ladder = None
                if wy+wh-BARREL_ONLADDER_DXINVERTINGHEIGHT[1] > by+bh > wy+wh-BARREL_ONLADDER_DXINVERTINGHEIGHT[0]:
                    self._dx*=-1
                if by+bh > wy+wh-BARREL_LADDEREND:
                    self._onLadder= False
                    self._ladder=None
            elif wy+wh >= by+bh >= wy and self._onFire and random.randint(0,2)==1:
                self._onLadder=True
                if self._dy>0:
                    self._dy*=-1
                if by+bh<wy+FIREBARREL_LADDEREND:
                    self._onLadder=False
                    self._ladder=None
                    if self._dy<0:
                        self._dy*=-1
                        self._dx*=-1


        if not self._onLadder:
            self._x += self._dx

    def rect(self):
        return self._x, self._y, self._w, self._h

    def collide (self,other):
        bx, by, bw, bh = self.rect()
        wx, wy, ww, wh = other.rect() # other's pos

        if (isinstance(other, Ladder)) and (wy <= by + bh <= wy + wh) and (wx < bx + bw // 2 < wx + ww):
            self._ladder = other
        elif (isinstance(other, interruptedLadder)) and (wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
            self._ladder = other
        elif isinstance(other, Platform) and not self._onLadder:
            if by + bh < wy + wh:
                self._y = wy - bh
                self._onPlatform = True

    def symbol(self):
        if(self._onFire):
            self._w=FIREBARREL_WIDTH
            self._h=FIREBARREL_HEIGHT
            if random.randint(0,2)==1:
                return FIREBARREL_SYMBOL[0]
            else:
                return FIREBARREL_SYMBOL[1]
        else:
            self._w=12
            self._h=12
            if (0<=self._x%8<2):
                return BARREL_SYMBOL[0]
            elif (2<=self._x%8<4):
                return BARREL_SYMBOL[1]
            elif (4<=self._x%8<6):
                return BARREL_SYMBOL[2]
            elif (6<=self._x%8<8):
                return BARREL_SYMBOL[3]


class oilBarrel(Actor):
    def __init__ (self,arena,x,y):
        self._x = x
        self._y = y
        self._arena=arena
        self._w= OIL_BARREL_WIDTH
        self._h= OIL_BARREL_HEIGHT
    def symbol (self):
        if random.randint(0,2)==1:
            return OIL_BARREL_SYMBOL[0]
        else:
            return OIL_BARREL_SYMBOL[1]
    def rect(self):
        return self._x, self._y, self._w, self._h
    def move(self):
        pass
    def collide(self, other):
        pass

def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.rect())
class Peach (Actor):
    def __init__ (self,arena,x,y):
        self._x = x
        self._y = y
        self._arena=arena
        self._w= PEACH_WIDTH
        self._h= PEACH_HEIGHT
        self._position=0
        arena.add(self)
    def symbol (self):
        if self._position==0:
            return PEACH_SYMBOL[0]
        elif self._position==1:
            return PEACH_SYMBOL[1]
        elif self._position==2:
            return PEACH_SYMBOL[2]
        else:
            return PEACH_SYMBOL[3]
    def updatePosition (self):
        self._position = random.randint(1,3)
    def rect(self):
        return self._x, self._y, self._w, self._h
    def move(self):
        pass
    def collide(self, other):
        pass

class DonkeyKong (Actor):
    def __init__ (self,arena,x,y):
        self._x = x
        self._y = y
        self._arena=arena
        self._w= DONKEYKONG_WIDTH
        self._h= DONKEYKONG_HEIGHT
        self._position = 2
        self._droppingBarrel=False
        arena.add(self)

    def symbol (self):
        if self._droppingBarrel:
            return DONKEYKONG_SYMBOL_DROPPING
        else:
            if self._position==1:
                return DONKEYKONG_SYMBOL[0]
            elif self._position==2:
                return DONKEYKONG_SYMBOL[1]
            else:
                return DONKEYKONG_SYMBOL[2]
    def updatePosition (self):
        self._position = random.randint(1,3)
    def rect(self):
        return self._x, self._y, self._w, self._h
    def move(self):
        pass
    def collide(self, other):
        wx, wy, ww, wh = other.rect() # other's pos
        if (isinstance(other,Barrel)):
            if(self._x+self._w<wx+6):
                self._droppingBarrel=False
            else:
                self._droppingBarrel=True


def main():
    global arena
    arena = Arena(320, 240,2)
    Jumper(arena, 50, 100)
    print_arena(arena)
    while input() != 'x':
        arena.move_all()
        print_arena(arena)

if __name__ == '__main__':
    main()
