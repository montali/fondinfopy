class Skyscrapers():
    def __init__(self):
        self._field=[[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0],[2,0,0,0,0],[0,0,0,3,0]]

    def play_at(self,x,y):
        if(x>0 and x<4) and (y>0 and y<4):
            self._field[x][y]+=1
            if self._field[x][y]>3:
                self._field[x][y]=0
        return
    def get_val(self,x,y):
        return str(self._field[x][y])

def main():
    game = Skyscrapers()
    while (input!='x'):
        x=int(input("x: "))
        y=int(input("y: "))
        game.play_at(x,y)
        for i in range(5):
            for j in range(5):
                print(game.get_val(i,j), end=' ')
            print('')

if __name__ == '__main__':
    main()
