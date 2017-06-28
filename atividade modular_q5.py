#5.Recebe uma velocidade em m/s, retorne esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
def Velocidade(metro):
    return  metro * 3.6
a = float(input("Digite a velocidade(m/s): "))
a = Velocidade(a)
print ("A velocidade em km/h equivale a ", a)
