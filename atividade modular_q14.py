def Dezenas(num):
    d = (num // 10) % 10
    return "O dígito das dezenas é o número %d" % (d)

num = int(input("Digite um número inteiro e com três dígitos: "))
print(Dezenas(num))
