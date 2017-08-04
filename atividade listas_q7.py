#07.Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene
#numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
def  notas():
    media = []
    i=1
    while i <=5:
        nota = float(input("Digite a nota do %dº aluno: " % i))
        i+=1
        media.append(nota)

    cont = 0
    for i in media:
        if i >= 7:
            cont+=1
    print("Numero de alunos que obtiveram media maior ou igual a 7: %d." % cont)
        
notas()
