from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_excluir_produto(object):
    def __init__(self):
        self.label_id_produto = QLabel()
        self.texto_id_produto = QLineEdit()
        self.botao_excluir_produto = QPushButton()
    # __init__

    def setupUi(self, tela_excluir_produto):
        icon = QIcon()
        icon.addFile(u"icones/icone_produto.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_excluir_produto.resize(274, 108)
        tela_excluir_produto.setMaximumSize(274, 108)
        tela_excluir_produto.setMinimumSize(274, 108)
        tela_excluir_produto.setWindowTitle(u"Excluir Produto")
        tela_excluir_produto.setWindowIcon(icon)

        self.label_id_produto = QLabel(tela_excluir_produto)
        self.label_id_produto.setGeometry(QRect(20, 10, 121, 21))
        self.label_id_produto.setFont(font)
        self.label_id_produto.setText(u"ID do produto:")

        self.texto_id_produto = QLineEdit(tela_excluir_produto)
        self.texto_id_produto.setGeometry(QRect(140, 10, 111, 22))
        self.texto_id_produto.setFont(font)
        self.texto_id_produto.setText(u"")
        self.texto_id_produto.setMaxLength(8)

        self.botao_excluir_produto = QPushButton(tela_excluir_produto)
        self.botao_excluir_produto.setGeometry(QRect(70, 50, 141, 41))
        self.botao_excluir_produto.setFont(font)
        self.botao_excluir_produto.setText(u"Excluir Produto")
    # setupUi


class CriarTelaExcluirProduto(QMainWindow, Ui_tela_excluir_produto):
    def __init__(self):
        super(CriarTelaExcluirProduto, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_id_produto.setText(u"")
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaExcluirProduto()
    window.mostrar_tela()
    sys.exit(app.exec_())
