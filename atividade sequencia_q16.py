#16. Efetue o cálculo e a apresentação do valor de uma
#prestação em atraso utilizando a fórmula PRETAÇÃO =
#VALOR + (VALOR * (TAXA / 100) * TEMPO)

valor = float(input("Digite o valor da prestação: "))
tempo = int(input("Digite o tempo de atraso: "))
taxa = float(input("Digite o valor da taxa de atraso: "))


prestac = valor + (valor *(taxa/100) * tempo)

print("O valor da prestação em atraso é R$ %.2f" %prestac)
