#15. Recebe um número no formato CDU e imprima na forma UDC. Exemplo: 123, sairá 321.
#O número deve ser armazenado em outra variável antes de ser impresso.
def CDU_UDC(num):
    centena = num//100
    dezena = (num%100)//10
    unidade = num%10
    udc = unidade*100 + dezena*10 + centena
    return "O valor invertido é: %d" % (udc)

num = int(input("Digite um número inteiro e com três dígitos: "))
print(CDU_UDC(num))
