#------------------------------
# Name: Esercizio 2.2
# Authors: Montali Simone,  Riccardo Fava
#------------------------------


list=[]
n=int(input("Inserisci un valore: "))
while n>=0:
    list.append(n)
    n=int(input("Inserisci un valore: "))
x=list[(len(list)-1)]
maggiori=0
for num in list:
    if num>x:
        maggiori+=1
print("Maggiori:",maggiori)
