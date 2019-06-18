#!/usr/bin/env python3
'''
@author  Riccardo Fava(287516), Simone Montali(288144)
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from constants import *

class Actor():
    '''Interface to be implemented by each game character
    '''
    def move(self):
        '''Called by Arena, at the actor's turn
        '''
        raise NotImplementedError('Abstract method')

    def collide(self, other: 'Actor'):
        '''Called by Arena, whenever the `self` actor collides with some
        `other` actor
        '''
        raise NotImplementedError('Abstract method')

    def rect(self) -> (int, int, int, int):
        '''Return the rectangle containing the actor, as a 4-tuple of ints:
        (left, top, width, height)
        '''
        raise NotImplementedError('Abstract method')

    def symbol(self) -> (int, int):
        '''Return the (x, y) position of current sprite, if it is contained in
        a larger image, with other sprites. Otherwise, simply return (0, 0)
        '''
        raise NotImplementedError('Abstract method')


class Arena():
    '''A generic 2D game, with a given size in pixels and a list of actors
    '''
    def __init__(self, width: int, height: int):
        '''Create an arena, with given dimensions in pixels
        '''
        self._w, self._h = width, height
        self._actors = []

    def add(self, a: Actor):
        '''Register an actor into this arena.
        Actors are blitted in their order of registration
        '''
        if a not in self._actors:
            self._actors.append(a)
        return a

    def remove(self, a: Actor):
        '''Cancel an actor from this arena
        '''
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        '''Move all actors (through their own move method).
        After each single move, collisions are checked and eventually
        the `collide` methods of both colliding actors are called
        '''
        actors = list(reversed(self._actors))
        for a in actors:
            previous_pos = a.rect()
            a.move()
            if a.rect() != previous_pos:  # optimization for stationary actors
                for other in actors:
                    # reversed order, so actors drawn on top of others
                    # (towards the end of the cycle) are checked first
                    if other is not a and self.check_collision(a, other):
                            a.collide(other)
                            other.collide(a)

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Check the two actors (args) for mutual collision (bounding-box
        collision detection). Return True if colliding, False otherwise
        '''
        x1, y1, w1, h1 = a1.rect()
        x2, y2, w2, h2 = a2.rect()
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2
            and a1 in self._actors and a2 in self._actors)

    def actors(self) -> list:
        '''Return a copy of the list of actors
        '''
        return list(self._actors)

    def size(self) -> (int, int):
        '''Return the size of the arena as a couple: (width, height)
        '''
        return (self._w, self._h)

class DKArena (Arena):
    def __init__ (self, width: int, height: int, difficulty: int):
        self._w, self._h = width, height
        self._actors = []
        self._difficulty=difficulty
        self._mario=Jumper(self, MARIO_START_X,MARIO_START_Y)
        self.add(oilBarrel(self,OIL_BARREL_X,OIL_BARREL_Y))
        self._Peach=Peach(self,PEACH_X,PEACH_Y)
        self._DonkeyKong=DonkeyKong(self,DONKEYKONG_X,DONKEYKONG_Y)
    def marioLeft(self):
        self._mario.go_left()
    def marioRight(self):
        self._mario.go_right()
    def marioUp (self):
        self._mario.go_up()
    def marioJump (self):
        self._mario.jump()
    def marioStay (self):
        self._mario.stay()
    def lost (self):
        if not (self._mario._alive):
            return True
        else:
            return False
    def dropBarrel (self):
        self.add(Barrel(self,BARREL_START_X,BARREL_START_Y))
    def updateActorsPosition (self):
        self._Peach.updatePosition()
        self._DonkeyKong.updatePosition()

    def won (self):
        if (self._mario._y<WINNING_HEIGHT-self._mario._h):
            return True
        else:
            return False
