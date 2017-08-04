#8.Leia uma lista de 5 números inteiros, mostre a soma, a multiplicação e os números.
def numeros():
    L = []
    i=1
    while i <=5:
        num = int(input("Digite %dº número: "  % i))
        i+=1
        L.append(num)
        
    soma = 0
    mult = 1
    for i in L:
        print(i, end="\n")
        soma+= i
        mult*=i
    
    print("A soma é: %d" % soma)
    print("A multiplicação é: %d" % mult)
        
numeros()
        
