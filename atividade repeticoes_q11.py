#11. Dado um país A, com 5.000.000 de habitantes e
#uma taxa de natalidade de 3% ao ano, e um país B
#com 7.000.000 de habitantes e uma taxa de
#natalidade de 2% ano ano. Calcular e imprimir o
#tempo necessário para que a população do país A
#ultrapasse a população do país B.
a = 5000000
b = 7000000

anos = 0

while a != b:

	a += 5000000 * 0.03
	b += 7000000 * 0.02

	anos += 1

print("Serão necessários %d anos." % anos)
