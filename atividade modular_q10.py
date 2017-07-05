#10. Escreva um algoritmo/programa que mostre
#o triplo de um número informados pelo usuário.
def Triplo(num):
    tri = num * 3
    return "O triplo do número %d é %d." % (num, tri)

num = float(input("Digite um número: "))
print(Triplo(num))
