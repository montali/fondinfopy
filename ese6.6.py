def analgramma (parola):
    parole=[]
    print(parola)
    if len(parola)==1:
        parole=[parola]
    else:
        for i,c in enumerate(parola):
            for anagramma in analgramma(parola[:i] + parola[i+1:]):
                parole+=anagramma

    return parole



print(analgramma("abc"))
