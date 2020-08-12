QntNum = input("Quantos numeros serao digitados: ")
cont = 1
y = []

for x in range (QntNum):
	number = input("Enter to {} Number: ".format(cont))
	y.append(number)
	cont = cont +1	

for i in range (QntNum -1):
	for o in range (QntNum -1):
		if y[o] > y[o + 1]:
			aux = y[o + 1]
			y[o + 1] = y[o]
			y[o] = aux
print (y)

	



	
	
