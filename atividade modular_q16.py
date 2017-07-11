#16.Recebe o valor do lado de um quadrado e imprima a sua área e o seu perímetro.
def Quadrado(lado):
    area = lado * lado
    perimetro = lado * 4
    return "A área do quadrado é: %d \nO perímetro do quadrado é: %d" % (area, perimetro)

lado = int(input("Digite o lado do quadrado: "))
print(Quadrado(lado))
