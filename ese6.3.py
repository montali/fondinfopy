


def smooth(lista,cols):
    listanuova=[0 for x in range(len(lista))]
    intorno=[0 for x in range(9)]
    for i in range(len(lista)):
        somma=0
        counter=0
        intorno[0]=(i-1-cols)
        intorno[1]=(i-cols)
        intorno[2]=i-cols+1
        intorno[3]=i-1
        intorno[4]=i
        intorno[5]=i+1
        intorno[6]=i+cols-1
        intorno[7]=i+cols
        intorno[8]=i+cols+1
        for num in intorno:
            if not((num//cols<0) or (num//cols>=(len(lista)//cols))) or((num%cols<0)or (num%cols>(cols))):
                somma+=lista[num]
                counter+=1
        listanuova[i]=somma/counter
    return listanuova
lista=[]
with open("input.txt", "r") as fail:
    for line in fail:
        numbers=line.split(",")
        for numero in numbers:
            lista.append(float(numero))
cols=int(input("Colonne: "))
autput=smooth(lista,cols)
with open("result.txt", "w+") as fail2:
    for i in range(0,len(autput)):
        fail2.write(str(autput[i]))
        if(i!=len(autput)-1):
            fail2.write(',')
