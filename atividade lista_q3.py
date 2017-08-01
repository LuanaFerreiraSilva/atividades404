#3. Leia uma lista de 10 números reais e mostre-os na ordem inversa.
numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    numeros[i] = int(input("Digite o número %d: " %(i + 1)))

numeros.reverse()
print(numeros)
