#8. Crie	uma	função	que	recebe	um	número	inteiro	e	retorne	a	mensagem	positivo,	negativo	ou	igual	a	zero,	de	
#acordo	com	o	valor	recebido
def num(x):

	if x == 0:

		return "igual a zero"

	elif x < 0:

		return "negativo"

	elif x > 0:

		return "positivo"

try:

	x = int(input("Forneça um valor inteiro: "))

	print("O número %d é %s." % (x, num(x)))

except:

	print("Não foi fornecido um valor inteiro.")
