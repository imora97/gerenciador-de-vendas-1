from qt_core import *

FILE_UI = 'view/cliente_page.ui'

class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
