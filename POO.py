class Personas:
	pass
	def __init__(self,nombre,cedula,telefono,email):
		self.nombre = nombre
		self.cedula = cedula
		self.telefono = telefono
		self.email = email
	
	def __str__(self):
		return f"Nombre: {self.nombre}, cedula: {self.cedula}, telefono: {self.telefono}, email: {self.email}"
	
	def cambiar_datos(self, nombre, cedula, telefono, email):
		self.nombre = nombre
		self.cedula = cedula
		self.telefono = telefono
		self.email = email
		
def agregar():
    nombre = input("Nombre: ")
    cedula = input("Cedula: ")
    telefono =input("Telefono: ")
    email = input("Email: ")
    usuario = Personas(nombre,cedula,telefono,email)
    listadepersonas.append(usuario)

def verc():
	for i in range(0,len(listadepersonas)):
		print(f"{i + 1}- {listadepersonas[i]}")

def eliminar():
	verc()
	opcion = input("Indique la posición del usuario que desea eliminar: ")
	opcion= int(opcion)
	opcion = opcion - 1
	listadepersonas.pop(opcion)

def modificar():
	verc()
	mod = int(input("Indica la posición del usuario que quieres modificar: "))
	nombre = input("Introduce  el nuevo nombre: ")
	telefono = input("Introduce el nuevo telefono:  ")
	cedula = input("Introduce la nueva cedula: ")
	email = input("Introduce el nuevo email: ")
	listadepersonas[mod - 1].cambiar_datos(nombre,cedula, telefono, email)
	

listadepersonas = []
	
while True:		
		
    print("----------Menu---------------------\n")
    print("A. Para agregar ")
    print("B. Para borrar")
    print("C. Para ver las personas agregadas ")
    print("D. Para modificar a algun usuario\n")
    print("Cualquier tecla para salir ")
    
    print("-----------------------------------")
    opc = input("Por favor seleccione una opción: ")
    if opc == "a":
    	agregar()
    elif opc == "b":
    	eliminar()
    elif opc == "c":
    	verc()
    elif opc == "d":
    	modificar()
    else:
    	break