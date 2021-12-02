# importar as libs do PyQt
from PyQt5.QtWidgets import QApplication, QPushButton
import sys

def click():
    print("olá, o botão foi pressionado...")

# cria a aplicação
app = QApplication(sys.argv)

# definir os widgets que aparecerão na tela
window = QPushButton("Click aqui!")
#colocar um evendo no botão
window.clicked.connect(click)
window.show() # carregar o elemento para a tela

#executar o aplicativo
app.exec()