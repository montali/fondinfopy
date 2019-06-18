class Skyscrapers():
    def __init__(self):
        #self._field=[[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0],[2,0,0,0,0],[0,0,0,3,0]]
        self._field=[[0,0,0,0,0],[0,1,2,3,1],[0,3,1,2,0],[2,2,3,1,0],[0,0,0,3,0]]
    def play_at(self,x,y):
        if(x>0 and x<4) and (y>0 and y<4):
            self._field[x][y]+=1
            if self._field[x][y]>3:
                self._field[x][y]=0
        return
    def get_val(self,x,y):
        return str(self._field[x][y])
    def finished(self):
        for i in range(1,4):
            for j in range(1,4):
                if(self._field[i][j]==0):
                    return False
        for i in range(1,4):
            for j in range(1,4):
                print(i,j)
                if(j>1):
                    print("primo")
                    print(self._field[i][0:j])
                    if (self._field[i][j] in self._field[i][0:j]):
                        return False
                print("secondo")
                if (self._field[i][j] in self._field[i][j+1:len(self._field[i])-1]):
                    return False

                if(i>1):
                    print(i,j)
                    print(self._field[0:i][j])
                    if (self._field[i][j] in self._field[0:i][j]):
                        return False
                print("quarto")
                if (self._field[i][j] in self._field[i+1:len(self._field)-1]):
                    return False
        max=0
        skyscrapers=0
        print("cimuicnidjdi")
        for i in range(1,4):
            if(self._field[1][i]>max):
                max=self._field
                skyscrapers+=1
        print(skyscrapers)
        if (skyscrapers!=3):
            return False
        print("vera prima riga")
        max=0
        skyscrapers=0
        for i in range(1,4):
            if(self._field[3][i]>max):
                max=self._field
                skyscrapers+=1
        if(skyscrapers!=2):
            return False
        print("vera seconda riga")
        max=0
        skyscrapers=0
        for i in range(1,4):
            if(self._field[i][3]>max):
                max=self._field
                skyscrapers+=1
        print("ce semo")
        if(skyscrapers==1):
            return True

def main():
    game = Skyscrapers()
    print(game.finished())
    for i in range(5):
        for j in range(5):
            print(game.get_val(i,j), end=' ')
        print('')
    while (input!='x'):
        x=int(input("x: "))
        y=int(input("y: "))
        game.play_at(x,y)
        for i in range(5):
            for j in range(5):
                print(game.get_val(i,j), end=' ')
            print('')
        print(game.finished())

if __name__ == '__main__':
    main()
