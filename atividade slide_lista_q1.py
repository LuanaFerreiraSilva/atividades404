#Calcule a média aritmética de um aluno que possui 7 notas.
#Use a estrutura de repetição mais adequada.

notas = [10, 10, 10, 10, 10, 10, 10]
soma = 0
i = 0
while i < 7:
    soma += notas[i]
    i += 1
print("Média: %.1f" %(soma/7))
