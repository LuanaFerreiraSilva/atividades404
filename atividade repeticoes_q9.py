#09. Criar um algoritmo que calcule a soma dos
#números pares entre 25 e 200.
soma = 0
x = []
 
for c in range(24,200,2):
 
	x.append(c)
 
for c in range(0,len(x)):
 
	soma += c
 
print("A soma dos números pares entre 25 e 200 é %d." % soma)
