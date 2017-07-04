#09.Recebe um número inteiro e imprima na tela seu antecessor e o seu sucessor.
def Ante_Suce(num):
    antecessor = (num - 1)
    sucessor = (num +1)
    
    return "O antecessor do número %d é %d e o sucessor é %d." % (num, antecessor, sucessor)

num = int(input("Digite um número: "))
print(Ante_Suce(num))
