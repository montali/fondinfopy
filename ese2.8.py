import game2d

def update():
    DX=5
    DY=5
    global x
    global y
    game2d.canvas_fill((255, 255, 255))
    game2d.draw_rect((0,0,255),(x,y,100,100))
    if x<1100:
        x+=DX
    if y<700:
        y+=DY

game2d.canvas_init((1200, 800))
x = 50
y = 50
game2d.set_interval(update, 1000 // 30)
