#09. Criar um algoritmo que calcule a soma dos
#números pares entre 25 e 200.
soma = 0
i = []
 
for n in range(24,200,2):
 
	i.append(n)
 
for n in range(0,len(i)):
 
	soma += n
 
print("A soma dos números pares entre 25 e 200 é %d." % soma)


