#10.Leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
def  ListaA():
    A = []
    i=1
    while i <=5:
        num = int(input("Digite o %dº número : " % i))
        i+=1
        A.append(num)
      
    quad = 0
    for i in A:
        quad+=(i**2)
    print("Soma dos quadrados dos elementos: %d " % quad)
        
ListaA()
