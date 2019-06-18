import random;

capra=False
lupo=False
cavoli=False
contadino=False

while (capra!=True or lupo!=True or contadino !=True or cavoli!=True):
    mossa=random.randint(0,4);
    if ((capra==cavoli and capra!=contadino) or (lupo==capra and capra!=contadino)):
        print ("Ricomincio")
        capra=False
        lupo=False
        contadino=False
        cavoli=False
    elif (capra==contadino and mossa==0):
        capra= not capra;
        contadino= not contadino;
        print("Sposto la capra a", capra)
    elif (cavoli==contadino and mossa==1):
        contadino= not contadino;
        cavoli=not cavoli;
        print("Sposto i cavoli a", cavoli)
    elif (lupo==contadino and mossa==2):
        contadino= not contadino;
        lupo= not lupo;
        print("Sposto il lupo a", lupo)
    elif (mossa==3):
        contadino=not contadino;
