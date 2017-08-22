#15.Entrar com um número e imprimir todos os seus divisores.

numero = int(input("Forneça um número inteiro: "))

print("Os divisores de %d são: " % numero, end = "")

if numero == 0:

	print("Todos os números reais diferentes de zero.")

elif numero > 0:

	for i in range(numero,1,-1):

		if numero % i == 0:

			print(i, end = ", ")

	print("1.")

elif numero < 0:

	for i in range(numero,0,1):

		if numero % i == 0:

			print(i, end = ", ")

	for i in range(1,abs(numero),1):

		if numero % i == 0:

			print(i, end = ", ")

	print("%d." % abs(numero))
