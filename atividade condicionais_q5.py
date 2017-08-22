#5.Crie uma função que	recebe um número por parâmetro e retorna o valor booleano verdadeiro se o número for par.

def Verdadeiro(num):

	return num % 2 == 0

try:

	num = int(input("Forneça um número inteiro: "))

	print(Verdadeiro(num))

except:

	print("Não foi fornecido um valor inteiro.")
