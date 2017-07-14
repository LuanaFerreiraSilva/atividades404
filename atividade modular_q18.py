#18. Recebe dois valores para as variáveis A e B, efetuar a troca dos valores de forma que
#a variável A passe a ter o valor de B e que a variável B passe a ter o valor de A. Mostrar
#na tela os valores trocados.
def Valores_Trocados(A, B):
    aux = B
    B = A
    A = aux
    return "Valores Trocados!\n A = %d\n B= %d" %(A, B)
A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))
print(Valores_Trocados(A, B))
