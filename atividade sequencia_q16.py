#16. Efetue o c�lculo e a apresenta��o do valor de uma
#presta��o em atraso utilizando a f�rmula PRETA��O =
#VALOR + (VALOR * (TAXA / 100) * TEMPO)

valor = float(input("Digite o valor da presta��o: "))
tempo = int(input("Digite o tempo de atraso: "))
taxa = float(input("Digite o valor da taxa de atraso: "))


prestac = valor + (valor *(taxa/100) * tempo)

print("O valor da presta��o em atraso � R$ %.2f" %prestac)
