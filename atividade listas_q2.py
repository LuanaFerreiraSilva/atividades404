#2.Leia uma lista de 5 números inteiros e mostre-os.
def numeros():
    N = []
    i = 1
    while i <= 5:
        num = int(input("Digite o número %d: " %i))
        N.append(num)
        i+=1
    return N
def mostrar(N):
    for i in N:
        print(i, end="  ")
mostrar(numeros())
