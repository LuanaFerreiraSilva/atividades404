#12. Escreva	uma	função	que	recebe	um	número	inteiro	e	retorna	a mensagem	“O	número	é	múltiplo	de	7”	ou	“O	
#número	não	é	múltiplo	de	7”.
def multiplicidade(x):

	if x % 7 == 0:

		return "O número é múltiplo de 7"

	else:

		return "O número não é múltiplo de 7"

try:

	x = int(input("Forneça um valor inteiro: "))

	print(multiplicidade(x))

except:

	print("Não foi fornecido um valor inteiro.")
