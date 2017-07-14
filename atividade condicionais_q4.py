#4.Faça uma função que recebe três números por parâmetro e imprime na tela em ordem crescente.
def Crescente(A, B, C):
    if A == B or A == C or B == C:
        return "Inválido! Números iguais!"
    if A > B and A > C and B > C:
        return "Ordem crescente: %d, %d, %d" %(C, B, A)
    elif A > B and A > C and C > B:
        return "Ordem crescente: %d, %d, %d" %(B, C, A)
    elif B > A and B > C and A > C:
        return "Ordem crescente: %d, %d, %d" %(C, A, B)
    elif B > A and B > C and C > A:
        return "Ordem crescente: %d, %d, %d" %(A, C, B)
    elif C > A and C > B and B > A:
        return "Ordem crescente: %d, %d, %d" %(A, B, C)
    else:
        return "Ordem Crescente: %d, %d, %d" %(B,A,C)
    
A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))
print(Crescente(A, B, C))
