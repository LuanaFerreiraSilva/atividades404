#10. Escreva	 uma	 função	 que	 recebe	 a	 distância	 (em	 Km)	 e	 o	 tempo	 (em	 horas)	 de	 uma	 viagem,	 e	 retorne	 a	
#velocidade	média	da	viagem
def vm(d, t):

	return d / t

d, t = float(input("Forneça os valores correspondentes à distância (em km) e ao tempo (em h), respectivamente, da viagem: ")), float(input())

vm = str(vm(d, t))
vm = vm.rstrip('0').rstrip('.')

print("A tua velocidade escalar média nessa viagem foi de %s km/h." % vm)
