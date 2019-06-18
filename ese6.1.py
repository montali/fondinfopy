#------------------------------
# Name: Esercizio 6.1
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

import time

class Person():
    def __init__(self,name,surname,dd,mm,yy):
        self._name=name
        self._surname=surname
        self._dd=dd
        self._mm=mm
        self._yy=yy

    def age (self):
        if (int(time.strftime('%m'))>self._mm):
            return int(time.strftime('%Y'))-self._yy
        elif (int(time.strftime('%m'))==self._mm) and (int(time.strftime('%d'))>=self._dd):
            return int(time.strftime('%Y'))-self._yy
        else:
            return int(time.strftime('%Y'))-self._yy-1



def main():
    name=input("Insirire nome: ")
    surname= input ("Inserire cognome: ")
    day = int(input("Giorno: "))
    month = int(input("Mese: "))
    year = int(input ("Inserire anno (YYYY): "))
    persona= Person(name,surname,day,month,year)
    print("Età: ", persona.age())


if __name__ == '__main__':
    main()
