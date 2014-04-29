"""

db.maquinas.insert({'_id' : 1300, 
					'monitor' : 
								{ 'Marca' : 'Gateway', 
								  'Modelo' : 'kx1517', 
								  'Numero_serie' : 'DFJJHR4878DK'}, 
					'teclado' : 
								{ 'Marca' : 'Dell', 
								  'Modelo' : '516x', 
								  'Numero_serie' : 'HFEHF774587ZXDS'}, 
					'cpu' : 
								{ 'Marca' : 'IBM', 
								  'Modelo' : 'ThinkCentre' , 
								  'Numero_serie' : 'FJKJIUF487548X'}, 
					'diadema' : 
								{ 'Marca' : 'Jabra', 
								  'Modelo' : 'sin informacion', 
								  'Numero_serie' : 'sin informacion'}, 
					'mouse' : 
								{ 'Marca' : 'Dell', 
								  'Modelo' : '48XZ', 
								  'Numero_serie' : 'sin informacion'}
					});

"""

import sys
from PySide.QtGui import QWidget, QTabWidget, QLabel, QTextEdit, QMainWindow, QApplication, QMessageBox, QIcon, QPushButton, QWorkspace
from PySide.QtCore import SIGNAL
from pymongo import MongoClient


class TabsInventario(QWidget, cadena):
	

	def __init__(self):
		
		QWidget.__init__(self)
		Tabs = QTabWidget()

		TabMonitor = QWidget()
		LabelMonitorMarca = QLabel(TabMonitor)
		LineEditMonitorMarca = QLineEdit(TabMonitor)
		LabelMonitorModelo = QLabel(TabMonitor)
		LineEditMonitorModelo = QLineEdit(TabMonitor)
		LabelMonitorNumeroSerie = QLabel(TabMonitor)
		LineEditMonitorNumeroSerie = QLineEdit(TabMonitor)
		PushButtonMonitor = QPushButton(TabMonitor)
		
		TabTeclado = QWidget()
		LabelTeclado = QLabel(TabTeclado)
		LineEditTeclado = QLineEdit(TabTeclado)
		LabelTeclado = QLabel(TabTeclado)
		LineEditTeclado = QLineEdit(TabTeclado)
		LabelTeclado = QLabel(TabTeclado)
		LineEditTeclado = QLineEdit(TabTeclado)
		PushButtonTeclado = QPushButton(TabTeclado)
		
		TabMouse = QWidget()
		LabelMouseMarca = QLabel(TabMouse)
		LineEditMouseMarca = QLineEdit(TabMouse)
		LabelMouseModelo = QLabel(TabMouse)
		LineEditMouseModelo = QLineEdit(TabMouse)
		LabelMouseNumeroSerie = QLabel(TabMouse)
		LineEditMouseNumeroSerie = QLineEdit(TabMouse)
		PushButtonMouse = QPushButton(TabMouse)

		TabCPU = QWidget()
		LabelCPUMarca = QLabel(TabCPU)
		LineEditCPUMarca = QLineEdit(TabCPU)
		LabelCPUModelo = QLabel(TabCPU)
		LineEditCPUModelo = QLineEdit(TabCPU)
		LabelCPUNumeroSerie = QLabel(TabCPU)
		LineEditCPUNumeroSerie = QLineEdit(TabCPU)
		PushButtonCPU = QPushButton(TabCPU)

		TabDiadema = QWidget()
		LabelDiademaMarca = QLabel(TabDiadema)
		LineEditDiademaMarca = QLineEdit(TabDiadema)
		LabelDiademaModelo = QLabel(TabDiadema)
		LineEditDiademaModelo = QLineEdit(TabDiadema)
		LabelDiademaNumeroSerie = QLabel(TabDiadema)
		LineEditDiademaNumeroSerie = QLineEdit(TabDiadema)
		PushButtonDiadema = QPushButton(TabDiadema)




		



class MainWindow(QMainWindow):


	def __init__(self):

		
		QMainWindow.__init__(self)
		Window = QWorkspace()
		Window.setWindowTitle('Inventario')
		self.setGeometry(500, 500, 300, 300)


	def setupComponents(self):

		
		btnAgregar = QPushButton('Agregar una maquina', self.Window)
		btnAgregar.move(50,50)
		btnAgregar.clicked.connect(self.AgregarMaquina())
		
		btnBuscar = QPushButton('Buscar una maquina', self.Window)
		btnBuscar.move(50,100)
		btnBuscar.clicked.connect(self.BuscarMaquina())


	def AgregarMaquina(self):

		WindowAgregar = QWidget()
		agregarlabel = QLabel()
		agregartextedit = QTextEdit()



	def errorDialog(self):

	
		QMessageBox.about(self, "Error de conexion", "Error al intentar conectar con la base de datos")


if __name__ == '__main__':
		
	App = QApplication(sys.argv)
	mainWindow = MainWindow()
	conn = MongoClient('mongodb://localhost:27017/')
	db = conn.inventario
	maquinas = db.maquinas
	print "La conexion ha sido exitosa"
	mainWindow.setupComponents()
	mainWindow.show()
	App.exec_()

	sys.exit(0)

	try:
		pass	
	

	except:

		mainWindow.errorDialog()



