#9.Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
#respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
def  Idade_Altura():
    idade = []
    altura = []
    i=1
    while i <=5:
        ida = int(input("Digite a idade: "))
        alt = float(input("Digite a altura: "))
        print("\n")
        i+=1
        idade.append(ida)
        altura.append(alt)

    idade.reverse()
    print("Idades Invertidas")
    print(idade)
    altura.reverse()
    print("Alturas Invertidas")
    print(altura)
             
Idade_Altura()
