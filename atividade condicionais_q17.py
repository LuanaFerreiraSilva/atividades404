#17. A	partir	de	dois	números	fornecidos	pelo	usuário,	escreva	uma	das	seguintes	mensagens:
#Os	dois	são	pares
#Os	dois	são	impares
#O primeiro	é	par	e	o	segundo	é	ímpar
#O	primeiro	é	ímpar	e	o	segundo	é	par
def dezessete(x, y):

	if x % 2 == 0 and y % 2 == 0:

		return "Os dois são pares"

	elif x % 2 != 0 and y % 2 != 0:

		return "Os dois são ímpares"

	elif x % 2 == 0 and y % 2 != 0:

		return "O primeiro é par e o segundo é ímpar"

	elif x % 2 != 0 and y % 2 == 0:

		return "O primeiro é ímpar e o segundo é par"

try:

	x, y = int(input("Forneça dois números inteiros: ")), int(input())

	print(dezessete(x, y))

except:

	print("Não foram fornecidos valores inteiros.")
