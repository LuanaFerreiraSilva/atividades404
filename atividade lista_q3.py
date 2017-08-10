#3. Leia uma lista de 10 números reais e mostre-os na ordem inversa.
def  Numeros():
    numeros = []
    i=1
    while i <=10:
        n = float(input("Digite o %dº número: " %i))
        i+=1
        numeros.append(n)
    
    numeros.reverse()
    print(numeros)

Numeros()
