from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_tela_alterar_dados(object):
    def __init__(self):
        self.texto_matricula = QLineEdit()
        self.label_matricula = QLabel()
        self.group_box_alterar_cargo = QGroupBox()
        self.radio_button_vendedor = QRadioButton()
        self.radio_button_gerente = QRadioButton()
        self.radio_button_entregador = QRadioButton()
        self.botao_alterar_dados = QPushButton()
    # __init__

    def setupUi(self, tela_alterar_dados):
        icon = QIcon()
        icon.addFile(u"icones/icone_login.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_alterar_dados.resize(411, 172)
        tela_alterar_dados.setMaximumSize(411, 172)
        tela_alterar_dados.setMinimumSize(411, 172)
        tela_alterar_dados.setWindowTitle(u"Alterar Dados")
        tela_alterar_dados.setWindowIcon(icon)

        self.texto_matricula = QLineEdit(tela_alterar_dados)
        self.texto_matricula.setGeometry(QRect(130, 20, 261, 21))
        self.texto_matricula.setFont(font)
        self.texto_matricula.setText(u"")
        self.texto_matricula.setMaxLength(20)

        self.label_matricula = QLabel(tela_alterar_dados)
        self.label_matricula.setGeometry(QRect(20, 20, 71, 16))
        self.label_matricula.setFont(font)
        self.label_matricula.setText(u"Matrícula:")

        self.group_box_alterar_cargo = QGroupBox(tela_alterar_dados)
        self.group_box_alterar_cargo.setGeometry(QRect(20, 50, 371, 61))
        self.group_box_alterar_cargo.setFont(font)
        self.group_box_alterar_cargo.setTitle(u"Alterar cargo")

        self.radio_button_vendedor = QRadioButton(self.group_box_alterar_cargo)
        self.radio_button_vendedor.setGeometry(QRect(10, 30, 91, 17))
        self.radio_button_vendedor.setText(u"Vendedor")

        self.radio_button_gerente = QRadioButton(self.group_box_alterar_cargo)
        self.radio_button_gerente.setGeometry(QRect(140, 30, 81, 17))
        self.radio_button_gerente.setText(u"Gerente")

        self.radio_button_entregador = QRadioButton(self.group_box_alterar_cargo)
        self.radio_button_entregador.setGeometry(QRect(250, 30, 101, 17))
        self.radio_button_entregador.setText(u"Entregador")

        self.botao_alterar_dados = QPushButton(tela_alterar_dados)
        self.botao_alterar_dados.setGeometry(QRect(130, 120, 141, 41))
        self.botao_alterar_dados.setFont(font)
        self.botao_alterar_dados.setText(u"Alterar dados")
    # setupUi


class CriarTelaAlterarDados(QMainWindow, Ui_tela_alterar_dados):
    def __init__(self):
        super(CriarTelaAlterarDados, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_matricula.setText(u"")
        self.radio_button_gerente.setChecked(False)
        self.radio_button_vendedor.setChecked(False)
        self.radio_button_entregador.setChecked(False)
        self.show()
    # mostrar_tela


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CriarTelaAlterarDados()
    window.show()
    sys.exit(app.exec_())
