#------------------------------
# Name: Esercizio 6.2
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

def binary (n: int):
    if(n==0):
        return ''
    else:
        if n%2==0:
            last='0'
        else:
            last='1'
        return binary(n//2) + last
