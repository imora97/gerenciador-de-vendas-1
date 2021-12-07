from controller.cad_peca import CadPecaWindow
from qt_core import *

FILE_UI = 'view/pecas.ui'


class PecaPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.peca_window = None

        # evento do botão nova peça
        self.novo_btn.clicked.connect(self.nova_peca)

    def nova_peca(self):
        # criação da janela de cadastro
        self.peca_window = CadPecaWindow()
        self.peca_window.show()
