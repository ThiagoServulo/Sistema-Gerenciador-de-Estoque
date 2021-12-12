from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tela_cadastrar_produto(object):
    def setupUi(self, tela_cadastrar_produto):
        icon = QIcon()
        icon.addFile(u"icones/icone_produto.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_cadastrar_produto.resize(404, 279)
        tela_cadastrar_produto.setMaximumSize(404, 279)
        tela_cadastrar_produto.setMinimumSize(404, 279)
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

        self.label_tamanho = QLabel(tela_cadastrar_produto)
        self.label_tamanho.setGeometry(QRect(20, 80, 91, 21))
        self.label_tamanho.setFont(font)
        self.label_tamanho.setText(u"Tamanho:")

        self.label_quantidade = QLabel(tela_cadastrar_produto)
        self.label_quantidade.setGeometry(QRect(20, 110, 91, 21))
        self.label_quantidade.setFont(font)
        self.label_quantidade.setText(u"Quantidade:")

        self.label_preco_compra = QLabel(tela_cadastrar_produto)
        self.label_preco_compra.setGeometry(QRect(20, 140, 131, 21))
        self.label_preco_compra.setFont(font)
        self.label_preco_compra.setText(u"Preço de compra:")

        self.label_preco_venda = QLabel(tela_cadastrar_produto)
        self.label_preco_venda.setGeometry(QRect(20, 170, 151, 21))
        self.label_preco_venda.setFont(font)
        self.label_preco_venda.setText(u"Preço de venda:")

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

        self.texto_tamanho = QLineEdit(tela_cadastrar_produto)
        self.texto_tamanho.setGeometry(QRect(160, 80, 221, 22))
        self.texto_tamanho.setFont(font)
        self.texto_tamanho.setText(u"")
        self.texto_tamanho.setMaxLength(50)

        self.spin_box_quantidade = QSpinBox(tela_cadastrar_produto)
        self.spin_box_quantidade.setGeometry(QRect(160, 110, 91, 22))
        self.spin_box_quantidade.setFont(font)
        self.spin_box_quantidade.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spin_box_quantidade.setMaximum(99999)

        self.double_spin_box_preco_compra = QDoubleSpinBox(tela_cadastrar_produto)
        self.double_spin_box_preco_compra.setGeometry(QRect(160, 140, 91, 22))
        self.double_spin_box_preco_compra.setFont(font)
        self.double_spin_box_preco_compra.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.double_spin_box_preco_compra.setMaximum(9999.99)

        self.double_spin_box_preco_venda = QDoubleSpinBox(tela_cadastrar_produto)
        self.double_spin_box_preco_venda.setGeometry(QRect(160, 170, 91, 22))
        self.double_spin_box_preco_venda.setFont(font)
        self.double_spin_box_preco_venda.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.double_spin_box_preco_venda.setMaximum(9999.99)

        self.botao_cadastrar_produto = QPushButton(tela_cadastrar_produto)
        self.botao_cadastrar_produto.setGeometry(QRect(110, 220, 201, 41))
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
        self.texto_tamanho.setText(u"")
        self.spin_box_quantidade.setValue(0)
        self.double_spin_box_preco_compra.setValue(0)
        self.double_spin_box_preco_venda.setValue(0)
        self.show()
    # mostrar_tela
