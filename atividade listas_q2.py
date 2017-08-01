#2.Leia uma lista de 5 números inteiros e mostre-os.
numeros = [0, 0 , 0 , 0, 0]

for i in range(5):
    numeros[i] = int(input("Digite o número %d: " %(i + 1)))

print("Os números foram: ", end="")
print(numeros)
