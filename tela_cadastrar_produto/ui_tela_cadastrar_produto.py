from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_cadastrar_produto(object):
    def __init__(self):
        self.label_descricao = QLabel()
        self.label_marca = QLabel()
        self.label_fabricante = QLabel()
        self.label_quantidade = QLabel()
        self.label_preco_compra = QLabel()
        self.texto_descricao = QLineEdit()
        self.texto_marca = QLineEdit()
        self.texto_fabricante = QLineEdit()
        self.spin_box_quantidade = QSpinBox()
        self.double_spin_box_preco_compra = QDoubleSpinBox()
        self.botao_cadastrar_produto = QPushButton()
    # __init__

    def setupUi(self, tela_cadastrar_produto):
        icon = QIcon()
        icon.addFile(u"icones/icone_produto.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_cadastrar_produto.resize(404, 236)
        tela_cadastrar_produto.setMaximumSize(404, 236)
        tela_cadastrar_produto.setMinimumSize(404, 236)
        tela_cadastrar_produto.setWindowTitle(u"Cadastrar Produto")
        tela_cadastrar_produto.setWindowIcon(icon)

        self.label_descricao = QLabel(tela_cadastrar_produto)
        self.label_descricao.setGeometry(QRect(20, 20, 91, 21))
        self.label_descricao.setFont(font)
        self.label_descricao.setText(u"Descrição:")

        self.label_marca = QLabel(tela_cadastrar_produto)
        self.label_marca.setGeometry(QRect(20, 50, 91, 21))
        self.label_marca.setFont(font)
        self.label_marca.setText(u"Marca:")

        self.label_fabricante = QLabel(tela_cadastrar_produto)
        self.label_fabricante.setGeometry(QRect(20, 80, 91, 21))
        self.label_fabricante.setFont(font)
        self.label_fabricante.setText(u"Fabricante:")

        self.label_quantidade = QLabel(tela_cadastrar_produto)
        self.label_quantidade.setGeometry(QRect(20, 110, 91, 21))
        self.label_quantidade.setFont(font)
        self.label_quantidade.setText(u"Quantidade:")

        self.label_preco_compra = QLabel(tela_cadastrar_produto)
        self.label_preco_compra.setGeometry(QRect(20, 140, 131, 21))
        self.label_preco_compra.setFont(font)
        self.label_preco_compra.setText(u"Preço de compra:")

        self.texto_descricao = QLineEdit(tela_cadastrar_produto)
        self.texto_descricao.setGeometry(QRect(160, 20, 221, 22))
        self.texto_descricao.setFont(font)
        self.texto_descricao.setText(u"")
        self.texto_descricao.setMaxLength(50)

        self.texto_marca = QLineEdit(tela_cadastrar_produto)
        self.texto_marca.setGeometry(QRect(160, 50, 221, 22))
        self.texto_marca.setFont(font)
        self.texto_marca.setText(u"")
        self.texto_marca.setMaxLength(50)

        self.texto_fabricante = QLineEdit(tela_cadastrar_produto)
        self.texto_fabricante.setGeometry(QRect(160, 80, 221, 22))
        self.texto_fabricante.setFont(font)
        self.texto_fabricante.setText(u"")
        self.texto_fabricante.setMaxLength(50)

        self.spin_box_quantidade = QSpinBox(tela_cadastrar_produto)
        self.spin_box_quantidade.setGeometry(QRect(160, 110, 91, 22))
        self.spin_box_quantidade.setFont(font)
        self.spin_box_quantidade.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spin_box_quantidade.setMaximum(99999)

        self.double_spin_box_preco_compra = QDoubleSpinBox(tela_cadastrar_produto)
        self.double_spin_box_preco_compra.setGeometry(QRect(160, 140, 91, 22))
        self.double_spin_box_preco_compra.setFont(font)
        self.double_spin_box_preco_compra.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.double_spin_box_preco_compra.setMaximum(9999.99)

        self.botao_cadastrar_produto = QPushButton(tela_cadastrar_produto)
        self.botao_cadastrar_produto.setGeometry(QRect(110, 180, 201, 41))
        self.botao_cadastrar_produto.setFont(font)
        self.botao_cadastrar_produto.setText(u"Cadastrar Produto")
    # setupUi


class CriarTelaCadastrarProduto(QMainWindow, Ui_tela_cadastrar_produto):
    def __init__(self):
        super(CriarTelaCadastrarProduto, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_descricao.setText(u"")
        self.texto_marca.setText(u"")
        self.texto_fabricante.setText(u"")
        self.spin_box_quantidade.setValue(0)
        self.double_spin_box_preco_compra.setValue(0)
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaCadastrarProduto()
    window.show()
    sys.exit(app.exec_())
