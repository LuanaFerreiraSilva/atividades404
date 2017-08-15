#14. Escreva um algoritmo que leia um conjunto de 100
#números inteiros positivos e determine o maior
#deles.
x = []

for c in range(100):

	x.append(int(input("X[%d] = " % c)))

x.sort()

print("\n%d" % x[99]) 
