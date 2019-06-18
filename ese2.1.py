#------------------------------
# Name: Esercizio 2.1
# Authors: Montali Simone,  Riccardo Fava
#------------------------------


stringa = input("Give me some testo: ")
cifre=0
len=0
for char in stringa:
    len+=1
    if(char>='0' and char <='9'):
        cifre+=1
print("La percentuale è", (cifre/len)*100,"%")

