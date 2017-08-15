#19. Escreva	uma	função	que	recebe	a	cor	de	um	sinal	de	trânsito	(“V”	é	verde;	“A”	é	amarelo;	“E”	é	vermelho)	e	
#retorne	a	respectiva	mensagem	“Siga”,	“Atenção”,	ou	“Pare”.	Assuma	entradas	válidas
def semaforo(cor):

	if cor == "V":

		return "Siga"

	elif cor == "A":

		return "Atenção"

	elif cor == "E":

		return "Pare"

cor = input("Forneça a letra correspondente à atual cor do semáforo (use 'V' para verde, 'A' para amarelo e 'E' para vermelho): ")

if semaforo(cor) == None:

	print("O caractere fornecido não corresponde a nenhuma cor. Tente novamente.")

else:

	print(semaforo(cor))
