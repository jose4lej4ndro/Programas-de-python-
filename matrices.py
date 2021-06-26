con1 = -1
con2= 0
matriz=[]
matriz2=[]
matrizr=[]
for i in range(0,3):
		matriz.append([0]*3)
		matriz2.append([0]*3)
		matrizr.append([0]*3)
		
opc = input("Elije una opción: 'a' para sumar, 'b' para restar o 'c' para multiplicar: ")
for i in range(0,3):
	for j in range(0,3):
		try:
			matriz[i][j]=int(input("Introduce la primera matriz: "))
		except:
			print("Por favor ingrese un numero")
			matriz[i][j]=int(input("Introduce la primera matriz: "))
		
for i in range(0,3):
	for a in range(0,3):
		try:
			matriz2[i][a]=int(input("Introduce la segunda matriz: "))
		except:
			print("Por favor ingrese un numero")
			matriz2[i][a]=int(input("Introduce la segunda matriz: "))

if opc == "a":	
	for i in range(0,3):
		for j in range(0,3):
			matrizr[i][j]= matriz[i][j]+matriz2[i][j]
elif opc == "b":
	for i in range(0,3):
		for j in range(0,3):
			matrizr[i][j]= matriz[i][j]-matriz2[i][j]
		
elif opc == "c":
	for x in range(0,3):
		for y in range(0,3):
			for z in range(0,3):
				matrizr[x][y]+= matriz[x][z] * matriz2[z][y]		

for a in range(0,3):
	r=[]
	for s in range(0,3):
		r.append(matrizr[a][s])
	print(r)