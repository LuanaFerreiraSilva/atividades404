#11.Faça um algoritmo para ler três números e exibir a soma
#do número 1 com o número 2, multiplicado pela soma do
#número 2 pelo 3.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

soma1 = num1 + num2
soma2 = num2 + num3
multiplicar = soma1 * soma2

print("O resultado é igual a: %d" %multiplicar)

