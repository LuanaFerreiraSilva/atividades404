#6. Crie	 uma	 função	 que	 recebe	 um	valor	 real	e	 retorna	a	mensagem	 “Vá	ao	 cinema”	 se	 o	valor	 recebido	 for	
#superior	a	R$	20,00	ou	“Fique	vendo	TV”	caso	contrário
def val(x):

	if x > 20:

		return "Vá ao cinema"

	else:

		return "Fique vendo TV"

try:

	x = float(input("Quanto dinheiro você tem (em R$): "))

	print(val(x))

except:

	print("Não foi fornecido um valor real.")
