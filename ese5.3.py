from ese52 import smooth
matrix=[]
i=0
with open("gesu.txt", "r") as fail:
    for line in fail:
        numbers=line.split(",")
        matrix.append([])
        for numero in numbers:
            matrix[i].append(float(numero))
        i+=1

print(smooth(matrix))
autput=smooth(matrix)
stringa=""
with open("result.txt", "w+") as fail2:
    for riga in autput:
        for numero in riga:
            fail2.write(str(numero))
            fail2.write(",")
        fail2.write("\n")
