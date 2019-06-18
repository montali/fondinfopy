import game2d

ARENA_W, ARENA_H= 320,240
W,H = 20,20

def update():
    global x, dx
    game2d.canvas_fill((255,255,255))
    game2d.draw_circle((255,0,0),(x,y),25)
    if not (0<=x + dx <= ARENA_W - W):
        dx = -dx
    x += dx

game2d.canvas_init((ARENA_W,ARENA_H))
x, y=50,75
dx = 5

game2d.set_interval(update,1000 // 30)
