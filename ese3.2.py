#------------------------------
# Name: Esercizio 3.2
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

import math

class Ellipsis:


    def __init__ (self,a: int,b: int):
        self._a=a
        self._b=b

    def area(self):
        return ((math.pi)*self._a*self._b)

    def focalDistance (self):
        return (2*(math.sqrt((self._a**2)-(self._b**2))))

def main ():
    a=int(input("Give me some a: "))
    b=int(input("Give me some b: "))
    ell1=Ellipsis(a,b)
    print("Area: ", ell1.area(), "Focal distance: ", ell1.focalDistance())
if __name__=="__main__":
    main()
