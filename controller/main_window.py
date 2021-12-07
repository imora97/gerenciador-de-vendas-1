# Classe que irá controlar o main_window.ui
from qt_core import *
from controller.clientes import ClientesPage
from controller.pecas import PecaPage
from controller.resumo import ResumoPage


FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        # criar os objetos referente as páginas
        self.resumo_page = ResumoPage()
        self.clientes_page = ClientesPage()
        self.peca_page = PecaPage()

        # Adicionar as páginas ao painel_principal
        self.painel_principal.insertWidget(0, self.resumo_page)  # pág 0
        self.painel_principal.insertWidget(1, self.clientes_page)
        self.painel_principal.insertWidget(2, self.peca_page)

        # define os eventos/ação dos botões
        self.resumo_btn.clicked.connect(self.show_resumo)
        self.clientes_btn.clicked.connect(self.show_clientes)
        self.pecas_btn.clicked.connect(self.show_pecas)

    def show_resumo(self):  # apresentar a tela de resumo no painel_principal
        self.painel_principal.setCurrentIndex(0)

    def show_clientes(self):
        self.painel_principal.setCurrentIndex(1)

    def show_pecas(self):
        self.painel_principal.setCurrentIndex(2)
