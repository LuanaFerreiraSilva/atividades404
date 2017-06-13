#20.Faça um algoritmo que efetue a apresentação do valor da
#conversão em real de um número lido em dólar. O
#programa lerá o calor da cotação do dólar e a quantidade
#de dólares com o usuário, para apresentar o valor em
#moeda brasileira.

Dolar = float(input("Digite o valor em dolar: "))

CotacaoDoDolar= 3.24
converter = Dolar / CotacaoDoDolar

print ("O valor correspondente em real(R$) é: %.2f" %converter)
