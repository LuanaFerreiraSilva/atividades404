#14.Crie uma função que	recebe	o ano de nascimento de uma pessoa e retorna uma	mensagem que diga se ela	
#poderá	ou não votar em	uma eleição para prefeito, não é necessário considerar o mês ou o dia que ela nasceu.

def Nascimento(ano):

	if 2020 - ano >= 16:

		return "Pode votar"

	else:

		return "Não pode votar"

try:

	ano1 = int(input("Forneça o valor correspondente ao  ano de nascimento: "))

	print(Nascimento(ano1))

except:

	print("Não foi fornecido um valor inteiro.")
