# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

import model.cliente_dao as funcoes_clientes
from model.cliente import Cliente
def carrega_dados():
    # ADCIONAR CLIENTES
    for i in range(0, 5):
        novo_cliente = Cliente(None, f'Cliente-{i}', 'rua alguma coisa', '75 9 8888888')
        # CHAMADA DA FUNÇÃO DE ADICIONAR UM CLIENTE EM CLIENTE_DAO.PY
        funcoes_clientes.adicionar(novo_cliente)
    # add peças



# cria a aplicação
app = QApplication(sys.argv)
carrega_dados()
# definir os widgets que aparecerão na tela
window = MainWindow()
window.show() # carregar o elemento para a tela

#executar o aplicativo
app.exec()