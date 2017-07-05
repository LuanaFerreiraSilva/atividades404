#13. Recebe o ano de nascimento de uma pessoa
#e escreva na tela a sua idade em 31/12/2013.
def AnoNascimento(ano):
    idade = 2013 - ano
    return " sua idade em 31/12/2013 era %d anos" % (idade)

try:   
    ano = int(input("Digite o seu ano de nascimento: "))
    print(AnoNascimento(ano))
except:
    print("Voce nao digitou um valor numérico!")
