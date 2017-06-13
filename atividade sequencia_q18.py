#18.Construa um algoritmo para ler os coeficientes do polinômio
#P(x) = Ax4 + Bx3 + Cx2 + Dx + E. Depois, leia o valor de x, calcule e imprima o valor de P(x).

print ("Resolvendo o polinômio P(x) = Ax4 + Bx3 + Cx2 + Dx + E")

A = float(input("Digite o valor para A: "))
B = float(input("Digite o valor para B: "))
C = float(input("Digite o valor para C: "))
D = float(input("Digite o valor para D: "))
E = float(input("Digite o valor para E: "))

A1 = A * 4
B1 = B * 3
C1 = C * 2

P = E / (A1 + B1 + C1 + D)

print ("O valor de x em P(x) = Ax4 + Bx3 + Cx2 + Dx + E é igual a: %.2f" %P)


