#03.Recebe um valor em minutos, retorna o equivalente em horas e minutos.
def hora_minutos(min):
    h = min // 60
    m = min % 60
    return "%d:%d" %(h,m)
print(hora_minutos(300))

