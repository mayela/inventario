from pymongo import MongoClient

def AgregarMaquina():
	
	maquina = {'id' : 0, 'monitor' : { 'marca' : None, 'modelo' : None, 'num_serie' : None}, 'teclado' : { 'marca' : None, 'modelo' : None, 'num_serie' : None}, 'mouse' : { 'marca': None, 'modelo' : None, 'num_serie' : None}, 'diadema' : {'marca' : None, 'modelo' : None, 'num_serie' : None}, 'cpu' : {'marca' : None, 'modelo' : None, 'num_serie' : 'None'}}

	maquina[id] = int(raw_input("Ingrese el identificador de la maquina: : "))
	
	# Datos de monitor

	maquina['monitor'] = raw_input( "Ingrese la marcar del monitor: ")

	raw_input( "Ingrese el modelo del monitor: ")

	raw_input( "Ingrese el numero de serie: ")
	
	# Datos de teclado

	raw_input( "Ingrese la marcar del monitor: ")

	raw_input( "Ingrese el modelo del monitor: ")

	raw_input( "Ingrese el numero de serie: ")
	
	# Datos de mouse

	raw_input( "Ingrese la marcar del monitor: ")

	raw_input( "Ingrese el modelo del monitor: ")

	raw_input( "Ingrese el numero de serie: ")
	
	# Datos de diadema

	raw_input( "Ingrese la marcar del monitor: ")

	raw_input( "Ingrese el modelo del monitor: ")

	raw_input( "Ingrese el numero de serie: ")
	
	# Datos de CPU

	raw_input( "Ingrese la marcar del monitor: ")

	raw_input( "Ingrese el modelo del monitor: ")

	raw_input( "Ingrese el numero de serie: ")

def BuscarMaquina():
	
try:
	conn = MongoClient('localhost', 27017)
	db = conn.inventario
	maquinas = db.maquinas
	while 1:
		print " 1. Agregar maquina"
		print " 2. Buscar maquina"
		print " 3. Editar maquina"
		print " 4. Salir"
		opc = int(raw_input("Elegir una opcion"))


		if opc == 1:
			Agregarmaquina()

		else if opc == 2:
			BuscarMaquina()

		else if opc == 3: 
			EditarMaquina()

		else if opc == 4:
			break

