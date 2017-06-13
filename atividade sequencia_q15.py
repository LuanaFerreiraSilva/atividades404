#Calcule e apresente o valor do volume de uma lata de óleo
#utilizando a fórmula: VOLUME = 3.14159 * RAIO / 2 * ALTURA.

print("Calculando o valor do volume de uma lata de óleo!")

ALTURA = float(input("Digite o valor do altura: "))
RAIO = float(input("Digite o valor do raio: "))

VOLUME = (3.14159 * RAIO )/(2 * ALTURA)

print("O volume da lata é igaul a: %f" %VOLUME)
