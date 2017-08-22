#12.Escreva uma função	que recebe um número inteiro e	retorna	a mensagem "O número é múltiplo	de 7" ou "O	
#número não é múltiplo de 7".
def Multiplo(numero):

	if numero % 7 == 0:

		return "O número é múltiplo de 7"

	else:

		return "O número não é múltiplo de 7"

try:

	numero = int(input("Digite um valor inteiro: "))

	print(Multiplo(numero))

except:

	print("Não foi fornecido um valor inteiro.")
