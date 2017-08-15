#14. Crie	uma	função	que	recebe	o	ano	de	nascimento	de	uma	pessoa	e	retorna	uma	mensagem	que	diga	se	ela	
#poderá	ou	não	votar	em	uma	eleição	para	prefeito,	não	é	necessário	considerar	o	mês	ou	o	dia	que	ela	nasceu.
def vot(ano):

	if 2020 - ano >= 16:

		return "Tu poderás votar"

	else:

		return "Tu não poderás votar"

try:

	a = int(input("Forneça o valor correspondente ao  ano de nascimento: "))

	print(vot(a))

except:

	print("Não foi fornecido um valor inteiro.")
