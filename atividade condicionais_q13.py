#13. Escreva	uma	função	que	retorne	“verdadeiro”	se	um	número	recebido	for	par	e	divisível	por	3.
def treze(x):

	return x % 2 == 0 and x % 3 == 0

try:

	x = int(input("Forneça um valor inteiro: "))

	print(treze(x))

except:

	print("Não foi fornecido um valor inteiro.")
