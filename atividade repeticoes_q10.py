#10. Criar um algoritmo que leia um número (n) e
#imprima a soma dos números múltiplos de 5 no
#intervalo aberto entre 1 e num. Suponha que n será
#maior que 1.
x = []
soma = 0
 
n = int(input("n = "))
 
i = 1
 
while i <= n:
 
	if i % 5 == 0:
 
  		soma += i
 
	i += 1
 
print("A soma dos números múltiplos de cinco no intervalo aberto entre 1 e %d é %d." % (n, soma))
