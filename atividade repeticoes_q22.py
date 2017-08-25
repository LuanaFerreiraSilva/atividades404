#22.Dados dois números inteiros positivos, determinar
#o máximo divisor comum entre eles usando o
#algoritmo de Euclides
def Algoritmo_Euclides(v1, v2):
    
    if v2 == 0:
        
        return v1
    
    else:
        
        return euclides(v2, v1 % v2)
 
v1, v2 = int(input("Digite dois números inteiros positivos: ")), int(input())

if v1 > 0 and v2 > 0:


	print("O MDC entre %d e %d é %d." % (v1, v2, Algoritmo_Euclides(v1, v2)))

else:

	print("Erro! Não foram digitados dois números inteiros e positivos .")
