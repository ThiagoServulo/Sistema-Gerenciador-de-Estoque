from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_relatorio_vendas_data(object):
    def __init__(self):
        self.calendario = QCalendarWidget()
        self.botao_confirmar = QPushButton()
    # __init__

    def setupUi(self, tela_relatorio_vendas_data):
        icon = QIcon()
        icon.addFile(u"icones/icone_relatorio.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_relatorio_vendas_data.resize(493, 360)
        tela_relatorio_vendas_data.setWindowTitle("Relatório de vendas")
        tela_relatorio_vendas_data.setMaximumSize(493, 360)
        tela_relatorio_vendas_data.setMinimumSize(493, 360)
        tela_relatorio_vendas_data.setWindowIcon(icon)

        self.calendario = QCalendarWidget(tela_relatorio_vendas_data)
        self.calendario.setGeometry(QRect(0, 0, 491, 281))
        self.calendario.setFont(font)

        self.botao_confirmar = QPushButton(tela_relatorio_vendas_data)
        self.botao_confirmar.setGeometry(QRect(130, 300, 211, 41))
        self.botao_confirmar.setFont(font)
        self.botao_confirmar.setText("Confirmar data")
    # setupUi


class CriarTelaSelecionarDataRelatorioVendas(QMainWindow, Ui_tela_relatorio_vendas_data):
    def __init__(self):
        super(CriarTelaSelecionarDataRelatorioVendas, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaSelecionarDataRelatorioVendas()
    window.mostrar_tela()
    sys.exit(app.exec_())
