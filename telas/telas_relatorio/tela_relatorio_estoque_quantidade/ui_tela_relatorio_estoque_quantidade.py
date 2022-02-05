from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_relatorio_estoque_quantidade(object):
    def __init__(self):
        self.spin_box_quantidade = QSpinBox()
        self.label_quantidade = QLabel()
        self.combo_box_tipo = QComboBox()
        self.label_tipo = QLabel()
        self.botao_gerar_relatorio_estoque_quantidade = QPushButton()
    # __init__

    def setupUi(self, tela_relatorio_estoque_quantidade):
        icon = QIcon()
        icon.addFile(u"icones/icone_relatorio.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_relatorio_estoque_quantidade.resize(208, 124)
        tela_relatorio_estoque_quantidade.setMaximumSize(208, 124)
        tela_relatorio_estoque_quantidade.setMinimumSize(208, 124)
        tela_relatorio_estoque_quantidade.setWindowTitle(u"Relatório de Estoque")
        tela_relatorio_estoque_quantidade.setWindowIcon(icon)

        self.botao_gerar_relatorio_estoque_quantidade = QPushButton(tela_relatorio_estoque_quantidade)
        self.botao_gerar_relatorio_estoque_quantidade.setGeometry(QRect(30, 70, 151, 41))
        self.botao_gerar_relatorio_estoque_quantidade.setFont(font)
        self.botao_gerar_relatorio_estoque_quantidade.setText(u"Gerar Relatório")

        self.label_tipo = QLabel(tela_relatorio_estoque_quantidade)
        self.label_tipo.setGeometry(QRect(10, 41, 131, 21))
        self.label_tipo.setFont(font)
        self.label_tipo.setText(u"Tipo:")

        self.combo_box_tipo = QComboBox(tela_relatorio_estoque_quantidade)
        self.combo_box_tipo.setGeometry(QRect(110, 40, 81, 22))
        self.combo_box_tipo.addItems([">", "<", "="])

        self.label_quantidade = QLabel(tela_relatorio_estoque_quantidade)
        self.label_quantidade.setGeometry(QRect(10, 10, 121, 21))
        self.label_quantidade.setFont(font)
        self.label_quantidade.setText(u"Quantidade:")

        self.spin_box_quantidade = QSpinBox(tela_relatorio_estoque_quantidade)
        self.spin_box_quantidade.setGeometry(QRect(110, 10, 81, 21))
        self.spin_box_quantidade.setFont(font)
        self.spin_box_quantidade.setMaximum(9999)
    # setupUi


class CriarTelaRelatorioProdutoQuantidade(QMainWindow, Ui_tela_relatorio_estoque_quantidade):
    def __init__(self):
        super(CriarTelaRelatorioProdutoQuantidade, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.spin_box_quantidade.setValue(0)
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaRelatorioProdutoQuantidade()
    window.mostrar_tela()
    sys.exit(app.exec_())
