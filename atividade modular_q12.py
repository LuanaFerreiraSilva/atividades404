#12.Recebe quatro números e imprima a média ponderada,
#sabendo-se que os pesos são respectivamente 1, 2, 3 e 4.
def MediaPonderada(num1, num2, num3, num4):
    
    ponderada = (num1*1)+(num1*2)+(num1*3)+(num1*4)/1+2+3+4
    
    return "A média ponderada dos números %d, %d, %d e %d com pesos, respectivos 1, 2, 3 e 4 é  %d." % (num1, num2, num3, num4, ponderada)

num1 = float(input("Digite um primeiro número: "))
num2 = float(input("Digite um segundo número: "))
num3 = float(input("Digite um terceiro número: "))
num4 = float(input("Digite um quarto número: "))

print(MediaPonderada(num1, num2, num3, num4))
