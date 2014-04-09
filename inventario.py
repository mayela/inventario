# -*- coding: utf-8 -*-
#hola mundo
from MySQLdb import connect
from PySide.QtGui import *
from PySide.QtCore import *
from sqlalchemy import *
import sys

class VentanaPrincipal(QMainWindow):
	""" Clase que construye una ventana principal.

	Con esta clase se creará una ventana y sobre ella se construirán las demás
	ventanas necesarias para dar de alta, buscar y editar la informacion
	de una maquina.

	"""

	def __init__(self):

		QMainWindow.__init__(self)
		
		#workspace = QWorkSpace()
		#workspace.setWindowTitle("Inventario")
		self.setWindowTitle("Inventario")
		
		
	def login(self):

		""" Funcion que coloca los widgets necesarios para el logeo dentro de la aplicacion.

		Esta funcion dibuja una pantalla de logeo con los elementos necesarias para
		ingresar la informacion.

		Args:
		
		Returns:

		Raises:

		"""
	
		ventana_logeo = QWidget()
		ventana_logeo.setWindowTitle("Login")
		ventana_logeo.setGeometry(300, 300, 1000, 800 )
	
		# Layout horizontal
		#horizontal_layout = QHBoxLayout(ventana_logeo)
	
		# Layout vertical 
		#vertical_layout = QVBoxLayout(ventana_logeo)

		# Imagen de usuario
		imagen_usuario = QIcon('contact-icon.png')
		label_imagen = QLabel('usuario', self)
		pixmap_imagen = imagen_usuario.pixmap(200, 200)
		label_imagen.setPixmap(pixmap_imagen)

	
		# Elementos del layout horizontal
	
	
		# Primera columna
		label_usuario = QLabel()
		label_usuario.setText("Usuario: ")
		label_passwd = QLabel()
		label_passwd.setText("Password: ")
		#horizontal_layout.addWidget(label_usuario)
		#horizontal_layout.addWidget(label_passwd)

		# Segunda columna 
		lineedit_usuario = QLineEdit()
		lineedit_passwd = QLineEdit()
		#self.echoLineEdit.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
		pushbutton_ingresar = QPushButton()
		#vertical_layout.addWidget(lineedit_usuario)
		#vertical_layout.addWidget(lineedit_password)
		#vertical_layout.addWidget(pushbutton_ingresar)

		ventana_logeo.show()


	def AgregarMaquina():
	
		""" Dibuja pantalla agregar maquina.

		Esta funcion proporciona al usuario una pantalla con pestanias
		para agregar la informacion necesaria para dar de alta una maquina.

		Args:
			db: Una conexion a base de datos realizada exitosamente.

		Returns:
		
		Raises:
		
		"""

		agregar_maquina = QTabWidget()
	
		# Layout horizontal 
		horizontal_layout = QHBoxLayout()

		# Layout vertical
		vertical_layout = QVBoxLayout()
		# Widgets necesarios para mostrar la tab informacion(id_maquina, perfil, sala)

		tab_info = QWidget()

		label_id = QLabel(tab_info)
		label_perfil = QLabel(tab_info)
		label_sala = QLabel(tab_info)

		lineedit_id = QLineEdit(tab_info)
		lineedit_perfil = QLineEdit(tab_info)
		lineedit_sala = QLineEdit(tab_info)

		label_id.setText("Id máquina: ")
		label_perfil.setText("Perfil: ")
		label_sala.setText("Sala: ")

		# Widgets necesarios para mostrar la tab monitor(marca, modelo, numero de serie)

		tab_monitor = QWidget()

		label_monitor_marca = QLabel(tab_monitor)
		label_monitor_modelo = QLabel(tab_monitor)
		label_monitor_numserie = QLabel(tab_monitor)

		lineedit_monitor_marca= QLineEdit(tab_monitor)
		lineedit_monitor_modelo = QLineEdit(tab_monitor)
		lineedit_monitor_numserie = QLineEdit(tab_monitor)

		label_monitor_marca.setText("Marca: ")
		label_monitor_modelo.setText("Monitor: ")
		label_monitor_numserie.setText("Número de serie: ")
		#lineedit.setText("algo de texto")

		# Widgets necesarios para mostrar la tab teclado(marca,modelo, numero de serie)
	
		tab_teclado = QWidget()

		label_teclado_marca = QLabel(tab_teclado)
		label_teclado_modelo = QLabel(tab_teclado)
		label_teclado_numserie = QLabel(tab_teclado)

		lineedit_teclado_marca= QLineEdit(tab_teclado)
		lineedit_teclado_modelo = QLineEdit(tab_teclado)
		lineedit_teclado_numserie = QLineEdit(tab_teclado)

		label_teclado_marca.setText("Marca: ")
		label_teclado_modelo.setText("Monitor: ")
		label_teclado_numserie.setText("Número de serie: ")

		# Widgets necesarios para mostrar la tab mouse(marca, modelo, numero de serie)
	
		tab_mouse = QWidget()

		label_mouse_marca = QLabel(tab_mouse)
		label_mouse_modelo = QLabel(tab_mouse)
		label_mouse_numserie = QLabel(tab_mouse)

		lineedit_mouse_marca= QLineEdit(tab_mouse)
		lineedit_mouse_modelo = QLineEdit(tab_mouse)
		lineedit_mouse_numserie = QLineEdit(tab_mouse)

		label_mouse_marca.setText("Marca: ")
		label_mouse_modelo.setText("Modelo: ")
		label_mouse_numserie.setText("Número de serie: ")
		# Widgets necesarios para mostrar la tab diadema(marca, modelo, numero de serie)
	
		tab_diadema = QWidget()

		label_diadema_marca = QLabel(tab_diadema)
		label_diadema_modelo = QLabel(tab_diadema)
		label_diadema_numserie = QLabel(tab_diadema)

		lineedit_diadema_marca= QLineEdit(tab_diadema)
		lineedit_diadema_modelo = QLineEdit(tab_diadema)
		lineedit_diadema_numserie = QLineEdit(tab_diadema)

		label_diadema_marca.setText("Marca: ")
		label_diadema_modelo.setText("Modelo: ")
		label_diadema_numserie.setText("Número de serie: ")
		# Widgets necesarios para mostrar la tab cpu(marca, modelo, numero de serie, so, ram, procesador)

		tab_cpu = QWidget()

		label_cpu_marca = QLabel(tab_cpu)
		label_cpu_modelo = QLabel(tab_cpu)
		label_cpu_numserie = QLabel(tab_cpu)

		lineedit_cpu_marca= QLineEdit(tab_cpu)
		lineedit_cpu_modelo = QLineEdit(tab_cpu)
		lineedit_cpu_numserie = QLineEdit(tab_cpu)

		label_cpu_marca.setText("Marca: ")
		label_cpu_modelo.setText("Monitor: ")
		label_cpu_numserie.setText("Número de serie: ")

		# Agregar todos los widget ventana al widget tab
		agregar_maquina.addTab(tab_info, "Información")
		agregar_maquina.addTab(tab_monitor, "Monitor")
		agregar_maquina.addTab(tab_teclado, "Teclado")
		agregar_maquina.addTab(tab_mouse, "Mouse")
		agregar_maquina.addTab(tab_diadema, "Diadema")
		agregar_maquina.addTab(tab_cpu, "CPU")

		maquina = {'id_maquina' : None, 'sala' : None, 'perfil' : None,
			   'monitor' : { 'marca' : None, 'modelo' : None, 'num_serie' : None},
			   'teclado' : { 'marca' : None, 'modelo' : None, 'num_serie' : None},
			   'mouse' : { 'marca': None, 'modelo' : None, 'num_serie' : None},
			   'diadema' : {'marca' : None, 'modelo' : None, 'num_serie' : None},
			   'cpu' : {'marca' : None, 'modelo' : None, 'num_serie' : None, 'so' : None, 'ram' : None, 'procesador': None}
			  }

		maquina[id_maquina] = raw_input("Ingrese el identificador de la maquina: : ")


		statement_maquina = """INSERT INTO maquina(Id_maquina, Sala, Perfil) VALUES(%s , %s, %s)""" %(maquina['id_maquina'], maquina['sala'], maquina['perfil'])
		statement_monitor = """INSERT INTO monitor(Id_maquina, Marca, Modelo, NumeroSerie) VALUES(%s, %s, %s, %s)""" %(maquina['id_maquina'], maquina['monitor']['marca'    ], maquina['monitor']['modelo'], maquina['monitor']['num_serie'])
		statement_teclado = """INSERT INTO teclado(Id_maquina, Marca, Modelo, NumeroSerie) VALUES(%s, %s, %s, %s)""" %(maquina['id_maquina'], maquina['teclado']['marca'    ], maquina['teclado']['modelo'], maquina['teclado']['num_serie'])
		statement_mouse = """INSERT INTO mouse(Id_maquina, Marca, Modelo, NumeroSerie) VALUES(%s, %s, %s, %s)""" %(maquina['id_maquina'], maquina['mouse']['marca'], maquina['mouse']['modelo'], maquina['mouse']['num_serie'])
		statement_diadema = """INSERT INTO diadema(Id_maquina, Marca, Modelo, NumeroSerie) VALUES(%s, %s, %s, %s)""" %(maquina['id_maquina'], maquina['diadema']['marca'    ], maquina['diadema']['modelo'], maquina['diadema']['num_serie'])
		statement_cpu = """INSERT INTO cpu(Id_maquina, Marca, Modelo, NumeroSerie, SistemaOperativo, Procesador, Ram) VALUES(%s, %s, %s, %s, %s, %s, %s)""" %(maquina['id_maquina'], maquina['cpu']['marca'], maquina['cpu']['modelo'], maquina['cpu']['num_serie'], maquina['cpu']['so'], maquina['cpu']['ram'], maquina['cpu']['procesador'])
		list_statements = [statement_maquina, statement_monitor, statement_teclado, statement_mouse, statement_diadema, statement_diadema, statement_cpu]
	
		for l in list_statements:
			db.execute(l)


	def BuscarMaquina(id):
		maquinas.find({'_id':id})

	
	def EditarMaquina(id,dict):
		maquinas.remove({'_id': id})
		maquinas.insert(dict)


app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.login()
try:
	ventana.show()
	app.exec_()
	sys.exit(0)

	#conn = connect(host= "localhost", port = 3306, user = "root", passwd = "toor", db = "inventario")

except: 
	
	print "Hubo un error al tratar de conectar con la base de datos"
