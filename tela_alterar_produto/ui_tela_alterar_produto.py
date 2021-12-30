from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_alterar_produto(object):
    def __init__(self):
        self.label_id_produto = QLabel()
        self.label_quantidade = QLabel()
        self.spin_box_quantidade = QSpinBox()
        self.botao_alterar_produto = QPushButton()
        self.texto_id_produto = QLineEdit()
    # __init__

    def setupUi(self, tela_alterar_produto):
        icon = QIcon()
        icon.addFile(u"icones/icone_produto.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_alterar_produto.resize(268, 134)
        tela_alterar_produto.setMaximumSize(268, 134)
        tela_alterar_produto.setMinimumSize(268, 134)
        tela_alterar_produto.setWindowTitle(u"Alterar Produto")
        tela_alterar_produto.setWindowIcon(icon)

        self.label_id_produto = QLabel(tela_alterar_produto)
        self.label_id_produto.setGeometry(QRect(20, 10, 121, 21))
        self.label_id_produto.setFont(font)
        self.label_id_produto.setText(u"ID do produto:")

        self.label_quantidade = QLabel(tela_alterar_produto)
        self.label_quantidade.setGeometry(QRect(20, 40, 91, 21))
        self.label_quantidade.setFont(font)
        self.label_quantidade.setText(u"Quantidade:")

        self.spin_box_quantidade = QSpinBox(tela_alterar_produto)
        self.spin_box_quantidade.setGeometry(QRect(140, 40, 101, 22))
        self.spin_box_quantidade.setFont(font)
        self.spin_box_quantidade.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spin_box_quantidade.setMaximum(99999)

        self.botao_alterar_produto = QPushButton(tela_alterar_produto)
        self.botao_alterar_produto.setGeometry(QRect(60, 80, 151, 41))
        self.botao_alterar_produto.setFont(font)
        self.botao_alterar_produto.setText(u"Alterar")

        self.texto_id_produto = QLineEdit(tela_alterar_produto)
        self.texto_id_produto.setGeometry(QRect(140, 10, 101, 22))
        self.texto_id_produto.setFont(font)
        self.texto_id_produto.setText(u"")
        self.texto_id_produto.setMaxLength(8)
    # setupUi


class CriarTelaAlterarProduto(QMainWindow, Ui_tela_alterar_produto):
    def __init__(self):
        super(CriarTelaAlterarProduto, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_id_produto.setText(u"")
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaAlterarProduto()
    window.mostrar_tela()
    sys.exit(app.exec_())
