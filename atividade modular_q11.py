#11.Recebe nome, endereço e telefone e imprima na tela.
def Nome_En_Tel(n, end, tel):
    
    return " Nome: %s \n Endereço: %s \n Telefone: %d " % (n, end, tel)

n = input("Digite o nome: ")
end = input("Digite o endereço: ")
tel = int(input("Digite o telefone: "))

print(Nome_En_Tel(n, end, tel))
