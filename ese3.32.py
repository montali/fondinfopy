def asterischiUpper (s):
    if(s[0]=='*'):
        inizio=True
    else:
        inizio=False
    s=s.split('*')
    if(inizio==True):
        i=0
    else:
        i=1
    print (s,inizio)
    while(i<(len(s))):
        s[i]=s[i].upper()
        i+=2
    return s


print(asterischiUpper("*Porco* *schifo* gesù"))
