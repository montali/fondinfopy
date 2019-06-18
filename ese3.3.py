
#------------------------------
# Name: Esercizio 3.3
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

def uppercase (s):
    sn=[]
    i=0
    asterix=False
    for x in (range(0,len(s))):
        if(s[x]=="*"):
            asterix= not asterix
        elif(asterix==True):
            sn.append(s[x].upper())
        else:
            sn.append(s[x])
    return ''.join(sn)



def main ():
    s=input("Inserire stringa asteriscata: ")
    print(uppercase(s))
if __name__=="__main__":
    main()
