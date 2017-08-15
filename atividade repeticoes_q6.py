#06. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
#usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print("Informe um nome de usuário e senha (Os valores não podem ser iguais)")
nome = input("\nNome de usuário: ")
senha = input("Senha: ")

while nome == senha:

	nome = input("Erro! Os valores não podem ser iguais.\nNome de usuário: ")
	senha = input("Senha: ")
print("Nome de usuário e senha criados com sucesso!")
