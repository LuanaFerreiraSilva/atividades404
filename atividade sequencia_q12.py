#12.Faça um algoritmo para ler dois números inteiro e exibir
#o resto da divisão do primeiro pelo segundo número.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resto = numero1 % numero2

print("O resto da divisão entre", numero1, "e", numero2, "é: %d" %resto)
