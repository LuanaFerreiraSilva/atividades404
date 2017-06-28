#06. Recebe uma velocidade em km/h, retorne esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
def Velocidadek(km):
    return  km / 3.6
a = float(input("Digite a velocidade(km/h): "))
a = Velocidadek(a)
print ("A velocidade em m/s equivale a ", a)
