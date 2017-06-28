#02.Recebe um valor em real (R$), retorna 70% deste valor.
def realPorc(x):
    return x * 0.7
a = float(input("Digite um valor: " ))
a = realPorc(a)
print("70 % do valor digitado eh igual a:", a)
