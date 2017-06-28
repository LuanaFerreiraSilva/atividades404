#07.Recebe 2 números, retorne a divisão da soma pela subtração dos números lidos.
def DiviSoma(a, b):
    d = (a+b)/(a-b)
    return "A divisao é %d" % d

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
print(DiviSoma(a, b))
        

