#17.Em época de pouco dinheiro os comerciantes estão procurando aumentar
#suas vendas oferecendo desconto. Recebe o valor de um produto e o percentual
#de desconto concedido e imprima o valor do produto com desconto.
def Desconto(v, d):
    desconto1 = d/100
    desconto2 = v*desconto1
    desconto3 = v - desconto2
    return "O valor do produto com desconto é R$ %.1f" %(desconto3)

v = float(input("Digite o valor do produto: "))
d = int(input("Digite o percentual de desconto: "))
print(Desconto(v,d))
