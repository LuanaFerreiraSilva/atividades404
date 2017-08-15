#11. Crie	 uma	 função	 que	 recebe	 a	 temperatura	 de	 uma	 pessoa	 e	 retorna	 “Está	 com	 febre”	 ou	 “Sem	 febre”.	
#Considere	o	valor	base	como	36.5.
def termometro(t):

	if t > 36.5:

		return "Está com febre"

	else:

		return "Sem febre"

try:

	t = float(input("Forneça um valor real correspondente à temperatura corporal de uma pessoa: "))

	print(termometro(t))

except:

	print("Não foi fornecido um valor real.")
