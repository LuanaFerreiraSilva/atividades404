#21.A imobiliária imobilis vende apenas terrenos retangulares.
#Faça um algoritmo para ler as dimensões de um terreno e,
#depois, exibir a área do terreno.

largura = float(input("Digite o valor da largura do terreno: "))
comprimento = float(input("Digite o valor do comprimento do terreno: "))

areaterreno = largura * comprimento

print("A área do terreno é: %.1f" %areaterreno)
