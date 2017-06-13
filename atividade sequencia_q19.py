#19.Leia uma temperatura em graus Celsius e apresente-a
#convertida em graus Fahrenheit. A fórmula de conversão
#é F = (9 * C + 160) / 5, sendo F a temperatura Fahrenheit
#e C a temperatura em Celsius.
print("Grau Celsius para Grau Fahrenheit")
grausCelsius = float(input("Digite o valor da temperatura em graus Celsius: "))

F = (9 * grausCelsius + 160) / 5

print("O valor correspondente em grau Fahrenheit é: %.2f" %F)
