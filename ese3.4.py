
#------------------------------
# Name: Esercizio 3.4
# Authors: Montali Simone,  Riccardo Fava
#------------------------------

def combinazione(s):
    x=[""]
    for i in range(0,len(s)):
        y=[]
        for j in range(0,len(s)):
            for k in range(0,len(s)):
                y.append(s[i])
                y.append(s[j])
                y.append(s[k])
                y.append(',')
        x.append(''.join(y))

    return x

print(combinazione("AEIOU"))
