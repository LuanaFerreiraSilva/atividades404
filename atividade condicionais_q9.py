#9. Escreva	uma	função	que	recebe	e	retorne	o	valor	booleano	“verdadeiro”	caso	o	número	seja	múltiplo	de	5,	ou	
#“falso”,	caso	contrário.
def multiplicidade(x):

	return x % 5 == 0

try:

	x = int(input("Forneça um valor inteiro: "))

	print(multiplicidade(x))

except:

	print("Não foi fornecido um valor inteiro.")
