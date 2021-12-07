from qt_core import *

FILE_UI = 'view/cad_peca.ui'


class CadPecaWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        # eventos dos botões
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)
    
    def fechar_janela(self):
        self.close() # close - fechar
    
    def salvar(self):
        # pega os dados
        nome = self.nome.text()
        validade = self.validade.value()
        valor = self.valor.text()

        #cria o objeto
