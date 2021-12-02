# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

# cria a aplicação
app = QApplication(sys.argv)

# definir os widgets que aparecerão na tela
window = MainWindow()
window.show() # carregar o elemento para a tela

#executar o aplicativo
app.exec()