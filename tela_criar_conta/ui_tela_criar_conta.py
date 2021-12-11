from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets


class Ui_tela_criar_conta(object):
    def setupUi(self, tela_criar_conta):
        icon = QIcon()
        icon.addFile(u"icones/icone_login.png", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)

        tela_criar_conta.setObjectName(u"tela_criar_conta")
        tela_criar_conta.resize(435, 263)
        tela_criar_conta.setMaximumSize(435, 263)
        tela_criar_conta.setMinimumSize(435, 263)
        tela_criar_conta.setWindowTitle(u"Criar Conta")
        tela_criar_conta.setWindowIcon(icon)

        self.centralwidget = QWidget(tela_criar_conta)

        self.botao_criar_conta = QPushButton(self.centralwidget)
        self.botao_criar_conta.setObjectName(u"botao_criar_conta")
        self.botao_criar_conta.setGeometry(QRect(140, 210, 161, 41))
        self.botao_criar_conta.setFont(font)
        self.botao_criar_conta.setText(u"Criar conta")

        self.texto_usuario = QLineEdit(self.centralwidget)
        self.texto_usuario.setGeometry(QRect(160, 19, 261, 21))
        self.texto_usuario.setFont(font)
        self.texto_usuario.setText(u"")
        self.texto_usuario.setMaxLength(40)

        self.label_nome = QLabel(self.centralwidget)
        self.label_nome.setGeometry(QRect(20, 20, 71, 16))
        self.label_nome.setFont(font)
        self.label_nome.setText(u"Nome:")

        self.texto_senha_1 = QLineEdit(self.centralwidget)
        self.texto_senha_1.setGeometry(QRect(160, 79, 261, 21))

        self.texto_senha_1.setFont(font)
        self.texto_senha_1.setText(u"")
        self.texto_senha_1.setMaxLength(20)
        self.texto_senha_1.setEchoMode(QLineEdit.Password)

        self.label_senha_1 = QLabel(self.centralwidget)
        self.label_senha_1.setGeometry(QRect(20, 80, 61, 16))
        self.label_senha_1.setFont(font)
        self.label_senha_1.setText(u"Senha:")

        self.label_senha_2 = QLabel(self.centralwidget)
        self.label_senha_2.setGeometry(QRect(20, 111, 131, 16))
        self.label_senha_2.setFont(font)
        self.label_senha_2.setText(u"Confirmar senha:")

        self.texto_senha_2 = QLineEdit(self.centralwidget)
        self.texto_senha_2.setGeometry(QRect(160, 110, 261, 21))
        self.texto_senha_2.setFont(font)
        self.texto_senha_2.setText(u"")
        self.texto_senha_2.setMaxLength(20)
        self.texto_senha_2.setEchoMode(QLineEdit.Password)

        self.label_email = QLabel(self.centralwidget)
        self.label_email.setGeometry(QRect(20, 51, 71, 16))
        self.label_email.setFont(font)
        self.label_email.setText(u"Email:")

        self.texto_email = QLineEdit(self.centralwidget)
        self.texto_email.setGeometry(QRect(160, 50, 261, 21))
        self.texto_email.setFont(font)
        self.texto_email.setText(u"")
        self.texto_email.setMaxLength(40)

        self.group_box_cargo = QGroupBox(self.centralwidget)
        self.group_box_cargo.setGeometry(QRect(20, 140, 401, 61))
        self.group_box_cargo.setFont(font)
        self.group_box_cargo.setTitle(u"Cargo")

        self.radio_button_vendedor = QRadioButton(self.group_box_cargo)
        self.radio_button_vendedor.setGeometry(QRect(30, 30, 101, 17))
        self.radio_button_vendedor.setText(u"Vendedor")

        self.radio_button_gerente = QRadioButton(self.group_box_cargo)
        self.radio_button_gerente.setGeometry(QRect(150, 30, 101, 17))
        self.radio_button_gerente.setText(u"Gerente")

        self.radio_button_entregador = QRadioButton(self.group_box_cargo)
        self.radio_button_entregador.setGeometry(QRect(260, 30, 121, 17))
        self.radio_button_entregador.setText(u"Entregador")

        tela_criar_conta.setCentralWidget(self.centralwidget)
    # setupUi


class CriarTelaCriarConta(QtWidgets.QMainWindow, Ui_tela_criar_conta):
    def __init__(self):
        super(CriarTelaCriarConta, self).__init__()
        self.setupUi(self)
    # __init__

    def mostrar_tela(self):
        self.texto_usuario.setText('')
        self.texto_email.setText('')
        self.texto_senha_1.setText('')
        self.texto_senha_2.setText('')
        self.radio_button_gerente.setChecked(False)
        self.radio_button_vendedor.setChecked(False)
        self.radio_button_entregador.setChecked(False)
        self.show()
    # mostrar_tela
