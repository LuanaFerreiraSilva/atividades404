#13.Faça um algoritmo para ler o salário de um funcionário e
#imprimir com um aumento de 15%.

salario = float(input("Digite o salário do funcionário: "))

percentual = (salario * 0.15) + salario


print("O valor do sálario com o aumento de é: %4.f" %percentual)
