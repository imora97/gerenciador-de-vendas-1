from qt_core import *

FILE_UI = 'view/cad_venda.ui'


class CadVenda(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
