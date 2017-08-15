#18. Crie	uma	função	que	recebe	três	valores	inteiros	e	retorna	o	maior	delas.	Suponha	não	haver	empates
def dezoito(x, y, z):

	nums = [x, y, z]

	nums.sort()

	return nums[2]

try:

	x, y, z = int(input("Forneça três valores inteiros: ")), int(input()), int(input())

	print("O maior dos três valores é %d." % dezoito(x, y, z))

except:

	print("Não foram fornecidos valores três inteiros.")
