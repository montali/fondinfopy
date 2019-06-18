def smooth (matrix):
    matricenuova=[[0 for x in range (len(matrix[0]))]for y in range (len(matrix))]
    intorno=[(0,0) for x in range(5)]
    somma=0
    counter=0
    print(len(matrix[0]))
    for i in range (0,len(matrix)):
        for j in range(0,len(matrix[0])):
            intorno[0]=(i-1,j)
            intorno[1]=(i+1,j)
            intorno[2]=(i,j-1)
            intorno[3]=(i,j+1)
            intorno[4]=(i,j)
            print(matrix[0][3])
            for num in intorno:
                if not (num[0]<0 or num[0] >= len(matrix) or num[1]<0 or num[1] >= len(matrix[0])):
                    print(num)
                    somma+=matrix[num[0]][num[1]]
                    counter+=1
            matricenuova[i][j]=somma/counter
            somma=0
            counter=0

    return matricenuova
