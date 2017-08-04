def notas():
    L = []
    i=1
    while i <=4:
        nota = float(input("Digite %dª nota: "  % i))
        i+=1
        L.append(nota)
        
    cont = 0
    
    for i in L:
        print(i, end="\n")
        cont+= i
    media = cont / len(L)
    print("A media e: %.1f" % media)
        
notas()
        
