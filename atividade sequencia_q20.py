#20.Fa�a um algoritmo que efetue a apresenta��o do valor da
#convers�o em real de um n�mero lido em d�lar. O
#programa ler� o calor da cota��o do d�lar e a quantidade
#de d�lares com o usu�rio, para apresentar o valor em
#moeda brasileira.

Dolar = float(input("Digite o valor em dolar: "))

CotacaoDoDolar= 3.24
converter = Dolar / CotacaoDoDolar

print ("O valor correspondente em real(R$) �: %.2f" %converter)
