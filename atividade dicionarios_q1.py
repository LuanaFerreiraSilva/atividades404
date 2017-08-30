#1.Crie um dicionário e armazene nele os seus dados: nome, idade, telefone, endereço. Imprima todos os
#dados usando o padrão chave: valor.

Dados = {"Nome" : "Luana Silva",
             "Idade" : 18,
             "Telefone" : "(86) 3212-5678",
             "Endereço" : "Quadra 1, Casa 12, Rua 123" }
 
for i in Dados:
    	print(i + ": %s" % Dados[i])
