stamping=0
frasi=[]
final=[]
with open("gesu.txt", "r") as fail:
    for line in fail:
        for char in line:
            if(char=='>'):
                stamping+=1
                final.append("".join(frasi))
                frasi=[]
            if(stamping%2==1):
                frasi.append(char)
            if(char=='<'):
                stamping+=1


for parola in final:
    print(parola,end='|')
