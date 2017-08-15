#5. Crie	uma	função	que	recebe	um	número	por	parâmetro	e	retorna	o	valor	booleano	verdadeiro	se	o	número	
#for	par.
def paridade(x):

	return x % 2 == 0

try:

	x = int(input("Forneça um número inteiro: "))

	print(paridade(x))

except:

	print("Não foi fornecido um valor inteiro.")
