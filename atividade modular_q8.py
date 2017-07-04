#08. Recebe 2 números inteiros, retorne o quociente e o resto da divisão do 1o pelo 2o. Recebe um número inteiro e imprima de
#volta na tela.
def Quociente_Resto(a, b):
    Q = (a/b)
    R = (a%b)
    
    return "O quociente da divisão é %d e o resto é %d." % (Q, R)

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
print(Quociente_Resto(a, b))
