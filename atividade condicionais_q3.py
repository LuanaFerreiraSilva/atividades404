#3.Faça	uma função que recebe dois números por parâmetro e retorna o maior.
def Numero_Maior(X, Y):
    valor='';
    if X > Y:
        return "O valor de X é maior que o de Y!\nx = %d" %(X)
    elif X < Y:
        return "O valor de Y é maior que o de X!\nY = %d" %(Y)
    else:
        return "Os valores de X e de Y são iguais!\nX = %d, y = %d" %(X,Y) 
      
X = int(input("Digite um valor para X: "))
Y = int(input("Digite um valor para Y: "))
print(Numero_Maior(X ,Y))
