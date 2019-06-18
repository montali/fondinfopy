def combina (wheels: int, elements: str):
    global lista
    if wheels==0:
        return
    for chars in elements:
        lista.append(chars)
        lista.append(combina(wheels-1, elements))
    return lista

lista=[]
print(combina(2,"AEI"))
